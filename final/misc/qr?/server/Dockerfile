FROM python:alpine3.10
RUN apk add --no-cache socat
COPY qrcode /usr/bin/
COPY flag.txt .
COPY script.sh .
CMD socat TCP-L:6996,fork EXEC:"./script.sh",reuseaddr,stderr
