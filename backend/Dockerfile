FROM python:3.10-slim

WORKDIR /app

COPY ./requirements.txt .

RUN pip install --trusted-host pypi.python.org -r requirements.txt

COPY . .

CMD [ "python3", "main.py"]