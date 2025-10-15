import React, { useRef } from 'react';
import { devPorts } from '../provider/devPorts';
import IndexNavbar from "../components/Navbars/IndexNavbar";
import DemoFooter from "../components/Footers/DemoFooter";
const Visualizer = () => {
      document.documentElement.classList.remove("nav-open");
  React.useEffect(() => {
    document.body.classList.add("index");
    return function cleanup() {
      document.body.classList.remove("index");
    };
  });
  const iframeRef = useRef(null);
  return (  <>
             <IndexNavbar/>
    <div className="page-header section-dark"
          style={{
            backgroundImage:
                "url(" + require("assets/img/MRIlocationsshot.jpg") + ")",
          }}>
      <iframe
        title="Niivue"
        ref={iframeRef}
        src={`http://localhost:${devPorts.niivue}`}
        style={{ width: '100%', height: '600px' }}
      />
    </div>
       <DemoFooter/>
            </>
  );
};

export default Visualizer;
