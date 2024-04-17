/*!

=========================================================
* Paper Kit React - v1.3.2
=========================================================

* Product Page: https://www.creative-tim.com/product/paper-kit-react

* Copyright 2023 Creative Tim (https://www.creative-tim.com)
* Licensed under MIT (https://github.com/creativetimofficial/paper-kit-react/blob/main/LICENSE.md)

* Coded by Creative Tim

=========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

*/
/*eslint-disable*/
import React from "react";

// reactstrap components
import {Button, Container} from "reactstrap";

// core components

function IndexHeader() {
  return (
    <>
      <div
          className="page-header section-dark"
          style={{
            backgroundImage:
                "url(" + require("assets/img/MRIlocationsshot.jpg") + ")",
          }}
      >
        <div className="filter"/>
        <div className="content-center">
          <Container>
            <div className="title-brand">
              <h1 className="presentation-title">HaN-Seg Challenge</h1>
              <div className="fog-low">
                <img alt="..." src={require("assets/img/fog-low.png")}/>
              </div>
              <div className="fog-low right">
                <img alt="..." src={require("assets/img/fog-low.png")}/>
              </div>
            </div>
            <h2 className="presentation-subtitle text-center">
              Segmentation for MR and CT!


            </h2>

          </Container>
        </div>


        <div
            className="moving-clouds"
            style={{
              backgroundImage: "url(" + require("assets/img/clouds.png") + ")",
            }}

        />

<div className="category category-absolute">
                      <Button
              className="btn-round"
              outline
              color="neutral"
              href="/register-page"
              size="lg"
              target="_blank"
          >
            Get Started
          </Button>
</div>
        <h6 className="category category-absolute">

          PFA 2 {" "}
          <a
              href="https://www.creative-tim.com?ref=pkr-index-page"
              target="_blank"
          >
            {/*<img*/}
            {/*    alt="..."*/}
            {/*    className="creative-tim-logo"*/}
            {/*    src={require("assets/img/creative-tim-white-slim2.png")}*/}
            {/*/>*/}
          </a>
        </h6>
      </div>
    </>
  );
}

export default IndexHeader;
