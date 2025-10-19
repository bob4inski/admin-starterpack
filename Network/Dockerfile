FROM ubuntu:24.04 AS base

RUN apt-get update \
    && apt-get install -y \
        iputils-ping \
        curl \
        net-tools \
        iproute2 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*


CMD [ "/bin/bash" ]
