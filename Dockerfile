# syntax=docker/dockerfile:1

#FROM python:3.6-slim-buster
#FROM ubuntu:16.04
FROM nvidia/cuda:9.0-cudnn7-devel-ubuntu16.04

WORKDIR /prj

COPY requirements.txt requirements.txt

RUN apt-get update -y && apt-get install -y software-properties-common && add-apt-repository ppa:deadsnakes/ppa

RUN apt-get update -y && apt-get install -y \
        python3.6 \
        python3-pip \
 && apt-get clean all


RUN apt-get install python3.6
RUN apt-get install unzip
#RUN apt-get install python3-pip
#RUN apt-get install -U python3-setuptools
RUN python3 -m pip install --upgrade "pip < 21.0"
RUN pip install -U setuptools
RUN python3 -m pip install -r requirements.txt

COPY . .

#CMD ["python3", "-m"]

