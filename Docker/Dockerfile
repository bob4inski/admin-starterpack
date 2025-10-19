FROM debian:bullseye-slim as base

RUN apt-get update && apt-get install -y nginx
COPY ./nginx.conf /etc/nginx/nginx.conf

CMD ["nginx", "-g", "daemon off;"]
