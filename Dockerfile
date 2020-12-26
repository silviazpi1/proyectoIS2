FROM python:latest

RUN apt update && \
    apt upgrade -y

RUN apt install -y python3 && \
    apt install -y python3-pip && \
    python3 -m pip install --upgrade pip

WORKDIR /proyectois2

COPY requirements.txt .
RUN python3 -m pip install -r requirements.txt

COPY src/ .
CMD [ "python3", "manage.py", "runserver", "0.0.0.0:80" ]