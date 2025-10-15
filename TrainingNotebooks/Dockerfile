ARG TF_SERVING_VERSION=latest
ARG TF_SERVING_BUILD_IMAGE=tensorflow/serving:${TF_SERVING_VERSION}-devel-gpu

FROM ${TF_SERVING_BUILD_IMAGE} as build_image
FROM nvidia/cuda:12.3.2-base-ubuntu22.04 as base_build

ARG TF_SERVING_VERSION_GIT_COMMIT=HEAD

VOLUME ["\\wsl.localhost\Ubuntu-22.04\home\aziz0220"]
WORKDIR /anaconda3/envs/py310

ENV CUDNN_VERSION=8.9.7.29
ENV TF_TENSORRT_VERSION=8.6.1
ENV CUDA=12.3
ENV LD_LIBRARY_PATH /usr/local/cuda/extras/CUPTI/lib64:$LD_LIBRARY_PATH

RUN apt-get update && apt-get install -y --no-install-recommends \
        curl

RUN curl -sSL --retry 5 https://raw.githubusercontent.com/tensorflow/serving/${TF_SERVING_VERSION_GIT_COMMIT}/tensorflow_serving/tools/docker/setup.sources.sh | sh

RUN apt-get install -y --no-install-recommends \
        ca-certificates \
        cuda-command-line-tools-12-3 \
        cuda-cupti-12-3 \
        cuda-libraries-12-3 \
        cuda-nvcc-12-3 \
        cuda-nvprune-12-3 \
        cuda-nvrtc-12-3 \
        libcublas-12-3 \
        libcudnn8=8.9.7.29-1+cuda12.3 \
        libcufft-12-3 \
        libcurand-12-3 \
        libcusolver-12-3 \
        libcusparse-12-3 \
        libnccl2=2.18.5-1+cuda12.2 \
        libnvinfer8=8.6.1.6-1+cuda12.0 \
        libnvinfer-plugin8=8.6.1.6-1+cuda12.0 \
        libgomp1 \
        build-essential \
        curl \
        libfreetype6-dev \
        pkg-config \
        software-properties-common \
        unzip



# Install TF Serving GPU pkg
COPY --from=build_image /usr/local/bin/tensorflow_model_server /usr/bin/tensorflow_model_server

# Expose ports
# gRPC
EXPOSE 8500

# REST
EXPOSE 8501

# Set where models should be stored in the container
ENV MODEL_BASE_PATH=/models
RUN mkdir -p ${MODEL_BASE_PATH}

# The only required piece is the model name in order to differentiate endpoints
ENV MODEL_NAME=model

# Create a script that runs the model server so we can use environment variables
# while also passing in arguments from the docker command line
RUN echo '#!/bin/bash \n\n\
tensorflow_model_server --port=8500 --rest_api_port=8501 \
--model_name=${MODEL_NAME} --model_base_path=${MODEL_BASE_PATH}/${MODEL_NAME} \
"$@"' > /usr/bin/tf_serving_entrypoint.sh \
&& chmod +x /usr/bin/tf_serving_entrypoint.sh

ENTRYPOINT ["/usr/bin/tf_serving_entrypoint.sh"]