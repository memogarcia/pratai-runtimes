FROM ubuntu:14.04

MAINTAINER Memo Garcia <sirmemogarcia@gmail.com>

RUN groupadd -r pratai -g 433 && \
useradd -u 431 -r -g pratai -d /home/ -s /sbin/nologin -c "Docker image user" pratai && \
chown -R pratai:pratai /home/

RUN apt-get -y update

RUN apt-get install -y git unzip wget