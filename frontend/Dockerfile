FROM node:14-alpine

RUN mkdir -p -- /app/src /app/public
WORKDIR /app

COPY package*.json ./

RUN npm install

EXPOSE 8080

CMD [ "npm", "run", "serve" ]
