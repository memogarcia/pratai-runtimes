FROM pratai/seed:latest

MAINTAINER Memo Garcia <sirmemogarcia@gmail.com>

RUN apt-get install -y python python-dev python-setuptools python-pip

RUN pip install pip --upgrade

COPY server.py server.py

RUN mkdir /etc/pratai/

RUN mkdir /var/log/pratai/