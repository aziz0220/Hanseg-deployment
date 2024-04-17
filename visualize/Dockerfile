FROM node:20.11.0
WORKDIR /app
COPY ./visualize/package*.json /.
RUN npm install
RUN npm install http-server
COPY ./visualize .
#visualizer
EXPOSE 5184
#uploadedfiles
EXPOSE 8050
#fileupload
EXPOSE 9000
CMD [ "npm","run", "dev:web" ]
