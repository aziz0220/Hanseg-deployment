import nrrd
from PIL import Image
import numpy as np
import os
import cv2
import SimpleITK as sitk
from matplotlib import pyplot as plt


global LABEL_dict
global SLICE_X
global SLICE_Y
global SLICE_Z
global rgb_codes
global case_names
SLICE_X = True
SLICE_Y = False
SLICE_Z = False
data_dir = '/mnt/c/Users/benam/Downloads/HaN-Seg/HaN-Seg/set_4/'
input_path = '/mnt/c/Users/benam/Downloads/HaN-Seg/HaN-Seg/set_2/'
case_names = [f"case_{num:02d}" for num in range(1, 43)]
LABEL_dict = {
    "background": 0,
    "A_Carotid_L": 1,
    "A_Carotid_R": 2,
    "Arytenoid": 3,
    "Bone_Mandible": 4,
    "Brainstem": 5,
    "BuccalMucosa": 6,
    "Cavity_Oral": 7,
    "Cochlea_L": 8,
    "Cochlea_R": 9,
    "Cricopharyngeus": 10,
    "Esophagus_S": 11,
    "Eye_AL": 12,
    "Eye_AR": 13,
    "Eye_PL": 14,
    "Eye_PR": 15,
    "Glnd_Lacrimal_L": 16,
    "Glnd_Lacrimal_R": 17,
    "Glnd_Submand_L": 18,
    "Glnd_Submand_R": 19,
    "Glnd_Thyroid": 20,
    "Glottis": 21,
    "Larynx_SG": 22,
    "Lips": 23,
    "OpticChiasm": 24,
    "OpticNrv_L": 25,
    "OpticNrv_R": 26,
    "Parotid_L": 27,
    "Parotid_R": 28,
    "Pituitary": 29,
    "SpinalCord": 30,
}
rgb_codes = [
    [255, 255, 255],  # Background
    [244, 214, 49],  # SpinalCord
    [216, 101, 79],  # A_Carotid_L
    [216, 101, 79],  # A_Carotid_R
    [183, 156, 220],  # Arytenoid
    [222, 198, 101],  # Bone_Mandible
    [145, 92, 109],  # Brainstem
    [178, 69, 182],  # BuccalMucosa
    [121, 39, 153],  # Cavity_Oral
    [104, 181, 63],  # Cochlea_L
    [123, 174, 91],  # Cochlea_R
    [220, 127, 211],  # Cricopharyngeus
    [174, 125, 64],  # Esophagus_S
    [127, 75, 38],  # Eye_AL
    [127, 75, 38],  # Eye_AR
    [53, 152, 174],  # Eye_PL
    [53, 152, 174],  # Eye_PR
    [86, 58, 127],  # Glnd_Lacrimal_L
    [86, 58, 127],  # Glnd_Lacrimal_R
    [222, 198, 101],  # Glnd_Submand_L
    [222, 198, 101],  # Glnd_Submand_R
    [62, 162, 114],  # Glnd_Thyroid
    [47, 210, 120],  # Glottis
    [150, 208, 243],  # Larynx_SG
    [188, 91, 95],  # Lips
    [99, 106, 24],  # OpticChiasm
    [127, 24, 70],  # OpticNrv_L
    [127, 24, 70],  # OpticNrv_R
    [31, 45, 172],  # Parotid_L
    [31, 45, 172],  # Parotid_R
    [57, 157, 110]
]

def fixSlice(slice, i):
    pre_width, pre_height = slice.shape
    slice = np.flipud(slice)
    image = Image.fromarray(slice)
    new_size = max(slice.shape[0], slice.shape[1])
    width, height = 512, 512
    image = image.resize((new_size, new_size), Image.NEAREST)
    left = (image.width - width) // 2
    top = (image.height - height) // 2
    right = left + width
    bottom = top + height
    image = image.crop((left, top, right, bottom))
    slice = np.array(image)
    fgs = Image.fromarray(slice)
    fout = os.path.join('./slices/', f'{i}.png')
    plt.imsave(fout, fgs, cmap='gray')
    image = cv2.imread(fout, cv2.IMREAD_COLOR)
    image = image / 255.0
    image = np.expand_dims(image, axis=0)
    image = image.astype(np.float32)
    return image, pre_width, pre_height

def sliceVolumeImage(vol):
    (dimx, dimy, dimz) = vol.shape
    sliced_data = []
    if SLICE_X:
        for i in range(dimx):
            img, pre_width, pre_height = fixSlice(vol[i, :, :], i)
            sliced_data.append((img, pre_width, pre_height))
    if SLICE_Y:
        for i in range(dimy):
            img, pre_width, pre_height = fixSlice(vol[:, i, :])
            sliced_data.append((img, pre_width, pre_height))
    if SLICE_Z:
        for i in range(dimz):
            img, pre_width, pre_height = fixSlice(vol[:, :, i])
            sliced_data.append((img, pre_width, pre_height))
    return sliced_data

def restoreSlice(slice, width, height):
    slice = np.flipud(slice)
    resize_shape = max(width, height)
    pad_width = ((resize_shape - slice.shape[0]) // 2, (resize_shape - slice.shape[1]) // 2)
    slice = np.pad(slice, pad_width=pad_width, mode='constant', constant_values=0)
    image = Image.fromarray(slice)
    image = image.resize((width, height), Image.NEAREST)
    image = image.rotate(90)
    slice = np.array(image)
    return slice

def restoreVolumeImage(slices, width, height, depth):
    volume = []
    if SLICE_X:
        print(len(slices), " === ", width)
        for i in range(width):
            slice = slices[i]
            volume.append(slice)
    if SLICE_Y:
        for i in range(height):
            slice = slices[i + width]
            volume.append(slice)
    if SLICE_Z:
        for i in range(depth):
            slice = slices[i + width + height]
            volume.append(slice)

    return np.stack(volume, axis=-1)

def grayscale_to_rgb(mask, rgb_codes):
    h, w = mask.shape[0], mask.shape[1]
    mask = mask.astype(np.int32)
    output = []
    for i, pixel in enumerate(mask.flatten()):
        output.append(rgb_codes[pixel])
    output = np.reshape(output, (h, w, 3))
    return output

def save_results(pred, save_image_path):
    pred = np.expand_dims(pred, axis=-1)
    pred = grayscale_to_rgb(pred, rgb_codes)
    cv2.imwrite(save_image_path, pred)

def normalizeImageIntensityRange(img, clip_min=0, shiftThreshold=1):
    minimg = min(img[img > 0].flatten())
    shifted_img = img.copy()
    if (minimg > shiftThreshold):
        shifted_img = shifted_img.astype(np.int16)
        shifted_img -= minimg
        shifted_img = np.clip(shifted_img, clip_min, None)
    return shifted_img
def center_crop_volumes(case_number):
    ct_image, mri_image, mask = load_data_sitk(case_number)
    mr_resampled = sitk.Resample(mri_image, ct_image)
    ct_array = sitk.GetArrayFromImage(ct_image)
    mri_array = sitk.GetArrayFromImage(mr_resampled)
    mask_array = sitk.GetArrayFromImage(mask)
    return ct_array, mri_array, mask_array

def load_data_sitk(case_number):
    CT_volume = sitk.ReadImage(input_path + f"/{case_names[case_number]}/{case_names[case_number]}_IMG_CT.nrrd")
    MR_volume = sitk.ReadImage(input_path + f"/{case_names[case_number]}/{case_names[case_number]}_IMG_MR_T1.nrrd")
    mask = sitk.ReadImage(
        input_path + f"/{case_names[case_number]}/{case_names[case_number]}_stacked_segments.seg.nrrd")
    return CT_volume, MR_volume, mask


def predict_case(model, nrrd_path, output_path, normalize=False, case_number=0):
    data, header = nrrd.read(nrrd_path)
    ct_image = sitk.ReadImage(nrrd_path)
    cropped_ct_image = sitk.GetArrayFromImage(ct_image)
    # CT_volume, MR_volume, mask = center_crop_volumes(case_number)
    cropped_mr_image = cropped_ct_image
    # cropped_ct_image, cropped_mr_image, cropped_mask = CT_volume, MR_volume, mask
    if normalize:
        cropped_mr_image = normalizeImageIntensityRange(cropped_mr_image)
    sliced_data = sliceVolumeImage(cropped_ct_image)
    predictions = []
    i = 0
    for image_slice in sliced_data:
        predicted_slice = model.predict(image_slice[0], verbose=0)[0]
        predicted_slice = np.argmax(predicted_slice, axis=-1)
        predicted_slice = predicted_slice.astype(np.uint8)
        save_image_path = f"predictions/{i}.png"
        save_results(predicted_slice, save_image_path)
        i += 1
        predicted_slice = restoreSlice(predicted_slice, image_slice[1], image_slice[2])
        predictions.append(predicted_slice)
    predicted_volume = restoreVolumeImage(predictions, data.shape[2], data.shape[1], data.shape[0])
    print(predicted_volume.shape)
    predicted_header = header.copy()
    nrrd.write(output_path, predicted_volume, predicted_header)

    print(f"Prediction saved to: {output_path}")
