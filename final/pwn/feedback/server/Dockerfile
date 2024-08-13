FROM python:alpine3.10
RUN apk add --no-cache socat libc6-compat
COPY . .
CMD socat TCP-L:1337,fork EXEC:"./feedback",reuseaddr,stderr
