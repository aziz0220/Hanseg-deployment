# HanSeg App

This directory contains the core components of the HanSeg web application for Head and Neck segmentation. It includes the React-based frontend, Flask backend for model predictions, Nginx for serving, and tools for visualization.

## Demo


<p align="center" style="width: 100%">
  <img src="public/demo.gif" alt="Demo" style="width: 80%"/>
</p>

## Directory Structure

- **app/**: React application source code.
- **flask/**: Flask API server handling model predictions and image processing.
- **nginx/**: Nginx configuration for proxying and serving static files.
- **public/**: Static assets, including the demo GIF and other public files.
- **visualize/**: Electron-based visualization tool using Niivue for 3D medical image rendering.
- **docker-compose.yaml**: Docker Compose file to orchestrate the services.

## How to Run

This application is designed to run as part of the overall HaNSeg deployment. From the root directory of the project, execute:

```bash
docker compose up
```

This will start all necessary services, including the web app, API, and visualization tools.

For development purposes, you can run individual components:

- **React App**: Navigate to `app/` and run `npm start`.
- **Flask API**: Navigate to `flask/` and run `python app.py`.
- **Visualization Tool**: Navigate to `visualize/` and follow its README.

## Requirements

- Docker and Docker Compose for full deployment.
- Node.js and npm for frontend development.
- Python and pip for backend development.
