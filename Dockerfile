FROM ubuntu:latest
MAINTAINER Wellington Castro "wcesarc@gmail.com"

RUN apt-get update
RUN apt-get install -y python-pip

RUN mkdir -p /opt/deploy/mentions_webpage
RUN mkdir -p /var/log/mentions_webpage/webserver/
RUN mkdir -p /var/log/mentions_webpage/application/

COPY . /opt/deploy/mentions_webpage
RUN pip install -r /opt/deploy/mentions_webpage/requirements.txt

WORKDIR /opt/deploy/mentions_webpage

RUN python manage.py collectstatic --noinput

EXPOSE 8002
