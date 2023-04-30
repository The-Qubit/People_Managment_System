FROM node:14-alpine

RUN mkdir -p -- /app/src /app/public
WORKDIR /app

COPY package-lock.json .
COPY package.json .

RUN npm install

COPY ./babel.config.js . 
COPY ./jsconfig.json .
COPY ./vue.config.js .

EXPOSE 8080

CMD [ "npm", "run", "serve" ]
