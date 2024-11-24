# HaNSeg Challenge Deployment

This project showcases the work done during the End of the 2nd Year Project, focusing on deploying a Head and Neck segmentation model as a web application. The model leverages deep learning techniques to predict segmentations of 31 organs at risk within the Head and Neck region, offering a practical tool for medical professionals.

---

## **Overview**
The project involves:
- Research on the Head and Neck segmentation challenge.
- Deployment of a deep learning model for segmentation.
- Development of a user-friendly web application integrating model predictions and visualization.

---

## **Requirements**
- **Docker**: For containerization and deployment.
- **Git**: For version control.

---

## **How to Run**
1. Clone the repository:
   ```bash
   git clone https://github.com/aziz0220/Hanseg_deployment_PFA.git
   ```
2. Start the application:
   ```bash
   docker compose up
   ```

---

## **Model Setup**
1. Download the latest deployed model from the OneDrive link:  
   **[Download Model](https://xbZFI4P_OoZffAB7zA?e=uJU3ne)**  
   *Note: Requires a domain account (@ensit.u-tunis.tn).*

2. Place the model in the following directory:
   ```
   ./Model Deployment (App)/flask/models/
   ```

---

## **Dataset and Challenge Links**
- Dataset: [Zenodo](https://zenodo.org/records/7442914#.ZBtfBHbMJaQ)
- HanSeg Challenge: [Grand Challenge](https://han-seg2023.grand-challenge.org/)

---

## **Presentation and Documentation**
- **Presentation**: [Canva Presentation](https://www.canva.com/design/DAGEqZ8TZBk/DxK6D0hUEfIaNvzxgVHNzg/edit?utm_content=DAGEqZ8TZBk&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)  
- **Report**: *([Google Drive PDF](https://drive.google.com/file/d/1cnl_MxjY2az77YfKjsEocIWOGFPp_VH7/view?usp=sharing))*  
- **Demo**: [Google Drive Video](https://drive.google.com/file/d/1NXzKlE1NUc4HEv-k1HjmkkVH2-kWk0Gl/view?usp=sharing)

---

## **Deployment Process**
1. **TensorFlow Serving**:
   - Used to deploy and test model versions in Docker containers.
2. **Performance Optimization**:
   - Reduced image processing time significantly using Flask and GPU optimizations.
3. **Visualization Integration**:
   - Leveraged **Niivue** for interactive 3D visualization of medical images.
4. **React Application**:
   - Developed a React-based web interface for seamless interaction with Flask and Niivue.


---

## **User Workflow**
1. Upload a 3D MR/CT image or a 2D image.
2. Image is pre-processed using Flask and sent to the TensorFlow Serving instance for prediction.
3. The predicted segmentation mask is returned and visualized interactively in the web application.

---

## **Acknowledgment**
This project was presented to the jury on **May 9, 2024**.

---

## **Future Work**
- Integrate additional features for clinical usability.
- Expand the model to support more segmentation tasks.

---

For more details, please refer to the [report](https://drive.google.com/file/d/1cnl_MxjY2az77YfKjsEocIWOGFPp_VH7/view?usp=sharing).
```
