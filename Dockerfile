FROM python:2.7.13-alpine
MAINTAINER Michael Porras

ENV LANG en_US.UTF-8


RUN mkdir -p /var/www/apium
WORKDIR /var/www/apium
ADD requirements.txt /var/www/apium/
RUN pip install -r requirements.txt
ADD . /var/www/apium
