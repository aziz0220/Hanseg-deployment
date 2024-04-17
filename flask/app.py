from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import tempfile
import tensorflow as tf
from predict_case import predict_case
import requests
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

app = Flask(__name__)
CORS(app, resources={r"/upload": {"origins": "*"}})

# Global variable to store the loaded model
model = None

def load_model():
    global model
    model_path = './models/model_3_epoch.h5'
    model = tf.keras.models.load_model(model_path)
    print("Model loaded successfully")

# Load the model when the server starts
load_model()

@app.route('/upload', methods=['POST'])
def upload_file():
    print("the request :" ,request.files)
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    # Save uploaded file to a temporary location
    temp_dir = tempfile.TemporaryDirectory()
    temp_file_path = os.path.join(temp_dir.name, file.filename)
    file.save(temp_file_path)
    prediction_path = os.path.join(temp_dir.name, 'prediction.nrrd')
    # Perform prediction using the global model
    predict_case(model, temp_file_path, prediction_path)
    server_url = 'http://hansegdeployment-visualize-1:9000/file'
    files = {'file': open(prediction_path, 'rb')}
    print("the files :", files)
    try:
        response = requests.post(server_url, files=files)
        response.raise_for_status()  # Raise an error if the response status is not successful
        print("File uploaded successfully!")
    except requests.exceptions.RequestException as e:
        print(f"Error uploading file: {e}")
        # Log the error or return an appropriate response to the client

        # Remove the temporary directory
    temp_dir.cleanup()
    # Return response
    return jsonify({'message': 'File uploaded and prediction completed'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)  # Change the port as needed
