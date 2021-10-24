# syntax=docker/dockerfile:1

FROM python:3.6-slim-buster

WORKDIR /prj

COPY requirements.txt requirements.txt

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "-m"]

