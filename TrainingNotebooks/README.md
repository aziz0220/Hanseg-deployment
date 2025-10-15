# Training Notebooks

This directory houses Jupyter notebooks used for the development, training, testing, and deployment of the HaNSeg model for Head and Neck segmentation.

## Notebooks Overview

- **3Dunet Training.ipynb**: Trains a 3D U-Net model on the HaNSeg dataset for segmenting 31 organs at risk in the Head and Neck region.
- **data_splitting.ipynb**: Handles the splitting of the dataset into training, validation, and test sets to ensure proper model evaluation.
- **deploy_model.ipynb**: Guides the deployment of the trained model using TensorFlow Serving for inference.
- **Han-Seg Dataset Cleaning.ipynb**: Performs data preprocessing, cleaning, and preparation of the HaNSeg dataset for training.
- **PFA2.ipynb**: Additional notebook for project-specific analysis, training iterations, or evaluations (refer to notebook content for details).
- **test_model_on_case_volume.ipynb**: Tests the deployed model on individual case volumes to validate performance and accuracy.

## Requirements

- **Jupyter Notebook** or **JupyterLab** for running the notebooks.
- **Python 3.x** with necessary libraries. Install dependencies using:

  ```bash
  pip install -r ../flask/requirements.txt
  ```

  Additional dependencies specific to notebooks may be listed within the notebooks themselves.

- **Docker** (optional): For containerized execution using the provided Dockerfile and docker-compose.yaml.

## How to Use

1. Ensure Python and required libraries are installed.
2. Launch Jupyter Notebook:

   ```bash
   jupyter notebook
   ```

3. Open the desired notebook and execute cells sequentially.
4. For Docker-based execution:

   ```bash
   docker compose up
   ```

   This sets up the environment for running notebooks in a container.

## Dataset

The notebooks utilize the HaNSeg dataset. Download from [Zenodo](https://zenodo.org/records/7442914#.ZBtfBHbMJaQ) and place in an appropriate directory as referenced in the notebooks.

## Model

Trained models can be downloaded from the provided OneDrive link in the main README and placed in `../flask/models/`.

