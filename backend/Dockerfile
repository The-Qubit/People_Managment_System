FROM python:3.10-slim

WORKDIR /app

RUN sh -c 'apt-get update'
RUN sh -c 'apt-get install -y curl gpg'
RUN sh -c 'curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor | tee /usr/share/keyrings/microsoft_windows_defender.gpg'
RUN sh -c 'echo " deb  [signed-by=/usr/share/keyrings/microsoft_windows_defender.gpg arch=amd64,armhf,arm64] https://packages.microsoft.com/ubuntu/22.04/prod jammy main" | tee /etc/apt/sources.list.d/microsoft-prod.list'
RUN sh -c 'curl https://packages.microsoft.com/config/debian/11/prod.list > /etc/apt/sources.list.d/mssql-release.list'
RUN sh -c 'apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EB3E94ADBE1229CF'
RUN sh -c 'apt-get update'
RUN sh -c 'ACCEPT_EULA=Y apt-get install -y msodbcsql17'

COPY ./requirements.txt .

RUN pip install --trusted-host pypi.python.org -r requirements.txt

COPY . .

EXPOSE 5000

CMD [ "python3", "app.py"]
