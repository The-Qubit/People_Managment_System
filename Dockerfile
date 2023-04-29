FROM python:3.10-slim

WORKDIR /app
COPY . .



EXPOSE 8080
CMD [ "python", "-d", "./frontend", "-m", "http.server", "8080" ]
