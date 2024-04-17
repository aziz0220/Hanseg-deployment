FROM node:20.11.0
WORKDIR /app
COPY ./app /.
RUN npm install
COPY ./app .
#mainapp
EXPOSE 3000
CMD [ "npm","run", "dev" ]
