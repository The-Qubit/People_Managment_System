FROM python:3.10-slim

WORKDIR /app
COPY . .

EXPOSE 8080
CMD [ "python", "-m", "http.server", "-d", "/app/frontend", "8080" ]
