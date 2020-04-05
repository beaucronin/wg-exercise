FROM ubuntu:latest

MAINTAINER Beau Cronin "beau.cronin@gmail.com"

RUN apt-get update -y && \
    apt-get install -y software-properties-common && \
    add-apt-repository -y ppa:deadsnakes/ppa && \
    apt-get update -y && \
    apt-get install -y python3.7 python3-pip python-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8
ENV FLASK_APP server/app.py
ENV FLASK_ENV development
ENV FLASK_DEBUG false

ENTRYPOINT [ "flask", "run", "-h", "0.0.0.0" ]
