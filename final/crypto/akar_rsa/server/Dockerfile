FROM python:alpine3.10
RUN apk add --no-cache socat \
    && pip3 install --upgrade pip \
    && pip3 install pycryptodome
COPY . .
CMD socat TCP-L:7489,fork EXEC:"timeout 60s ./chall.py",reuseaddr,stderr
