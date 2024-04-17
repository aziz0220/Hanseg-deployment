import React, { useState, useRef } from "react";
import { devPorts } from '../../provider/devPorts';
import { Container, Row, Col, Button } from "reactstrap";
import axios from "axios";

function SectionDark() {
  const [file, setFile] = useState(null);
  const [msg, setMsg] = useState("");
  const [showIframe, setShowIframe] = useState(false); // State variable for iframe visibility

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handlePredict = () => {
    if (!file) {
      setMsg("Please select a file.");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);
    // formData.append("output_path", "/mnt/c/Users/benam/OneDrive - Ministere de l'Enseignement Superieur et de la Recherche Scientifique/Desktop/paper-kit-react-main/paper-kit-react-main/src/results/prediction.nrrd");

    axios
      .post("http://localhost:80/flask", formData)
      .then((res) => {
        setMsg("Prediction completed. Check results.");
        setShowIframe(true); // Show the iframe after prediction
        console.log(res.data);
      })
      .catch((err) => {
        setMsg("Error predicting. Please try again.");
        console.error(err);
      });
  };

  const iframeRef = useRef(null);

  return (
    <>
      <div className="section section-dark">
        <Container>
          <Row>
            <Col className="ml-auto mr-auto text-center" md="8">
              <h2 className="title">Try out our SEGMENTATION MODEL</h2>
              <p className="description">
                Upload an image to predict segmentation.
              </p>
            </Col>
          </Row>
          <Row>
            <Col className="ml-auto mr-auto text-center" md="8">
              <input type="file" onChange={handleFileChange} />
              <Button
                className="btn-round ml-1"
                color="danger"
                outline
                onClick={handlePredict}
              >
                PREDICT
              </Button>
            </Col>
          </Row>
          <Row>
            <Col className="ml-auto mr-auto text-center" md="0">
              {msg && <p className="text-danger">{msg}</p>}
              {/* Display the iframe if showIframe is true */}
              {showIframe && (
                <iframe
                  title="Niivue"
                  ref={iframeRef}
                  src={`http://localhost:${devPorts.niivue}`}
                  style={{
                    width: "100%",
                    height: "600px",
                    border: "none",
                  }}
                />
              )}
            </Col>
          </Row>
        </Container>
      </div>
    </>
  );
}

export default SectionDark;
