# syntax=docker/dockerfile:1

#FROM ubuntu:16.04
FROM nvidia/cuda:9.0-cudnn7-devel-ubuntu16.04

WORKDIR /prj

COPY requirements.txt requirements.txt


RUN apt-get update \
 && apt-get install --assume-yes --no-install-recommends --quiet \
        python3 \
        python3-pip \
 && apt-get clean all

RUN python3 -m pip install --upgrade "pip < 21.0"
RUN pip install -U setuptools
RUN python3 -m pip install -r requirements.txt

COPY . .
