import React, { forwardRef, useState, useRef } from "react";
import { devPorts } from '../../provider/devPorts';
import { Container, Row, Col, Button } from "reactstrap";
import axios from "axios";
import Box from '@mui/material/Box';
import CircularProgress from '@mui/material/CircularProgress';
import { green } from '@mui/material/colors';
import CloudUploadIcon from '@mui/icons-material/CloudUpload';
import StopCircleIcon from '@mui/icons-material/StopCircle';
import Fab from '@mui/material/Fab';
import CheckIcon from '@mui/icons-material/Check';
import SaveIcon from '@mui/icons-material/Save';
function SectionDark() {
  const [file, setFile] = useState(null);
  const [msg, setMsg] = useState("");
  const [showIframe, setShowIframe] = useState(false); // State variable for iframe visibility
  const hiddenFileInput = useRef(null);
 const [showPredictButton, setShowPredictButton] = useState(true); // State for button visibility
  const [loading, setLoading] = React.useState(false);
  const [success, setSuccess] = React.useState(false);
    const [startTime, setStartTime] = useState(null);
  const timer = React.useRef();

    const buttonSx = {
    ...(success && {
      bgcolor: green[500],
      '&:hover': {
        bgcolor: green[700],
      },
    }),
  };

      React.useEffect(() => {
    return () => {
      clearTimeout(timer.current);
    };
  }, []);
  const handleClick = () => {
    hiddenFileInput.current.click(); // Trigger file selection dialog
  };

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
     setShowPredictButton(false);
  };

  const handlePredict = () => {
  if (!loading) {
       setSuccess(false);
      setLoading(true);

    if (!file) {
      setShowIframe(false);
      setMsg("Please select a file.");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);
    axios
      .post("http://localhost:80/flask", formData)
      .then((res) => {
        setMsg("Prediction completed. Check results.");



        setShowIframe(true);
        console.log(res.data);
        setSuccess(true);
        setLoading(false);
        timer.current = setTimeout(() => {
        setShowPredictButton(true);
      }, 4000);
      })
      .catch((err) => {
        setMsg("Error predicting. Please try again.");
        console.error(err);
      });}

  };

  const iframeRef = useRef(null);

  return (
    <>
      <div id="section-dark" className="section section-dark">
        <Container>
          <Row>
            <Col className="ml-auto mr-auto text-center" md="8">
              <h2 className="title">Try out our SEGMENTATION MODEL</h2>
         <p className="description" style={{ display: showPredictButton ? 'inline-block' : 'none' }}>
                Upload an image to predict segmentation.
              </p>
            </Col>
          </Row>
          <Row>
                    <Col className="ml-auto mr-auto text-center" md="8">
              {showPredictButton && ( // Conditionally render CloudUploadIcon
                <CloudUploadIcon fontSize="large" style={{ marginRight: 10 }} onClick={handleClick} />
              )}
              <input
                type="file"
                ref={hiddenFileInput}
                onChange={handleFileChange}
                style={{ display: "none" }} // Hide the default input
              />
                <Box sx={{ m: 1, position: 'relative' }}>
              <Button
                variant="contained"
                sx={buttonSx}
                className="btn-round ml-1"
                color="danger"
                outline
                disabled={loading}// Disable predict button if no file selected
                onClick={handlePredict}
                style={{ display: showPredictButton ? 'none' : 'inline-block' }} // Conditionally show predict button
              >
                PREDICT
              </Button>
                      {loading && (
          <CircularProgress
            size={24}
            sx={{
              color: green[500],
              position: 'absolute',
              top: '50%',
              left: '50%',
              marginTop: '-12px',
              marginLeft: '-12px',
            }}
          />
        )}
                            </Box>
            </Col>
          </Row>
          <Row>
            <Col className="ml-auto mr-auto text-center" md="0">
              {msg && <p className="text-danger">{msg}</p>}
              {/* Display the iframe if showIframe is true */}

            </Col>
          </Row>
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
        </Container>

      </div>

    </>

  );
}

export default  SectionDark;
