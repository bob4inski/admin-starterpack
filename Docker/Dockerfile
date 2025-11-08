FROM ubuntu:24.04 AS base

RUN apt-get update \
    && apt-get install -y nginx

COPY ./nginx.conf /etc/nginx/nginx.conf

WORKDIR /tmp

RUN apt install -y net-tools

CMD ["/bin/bash"]
