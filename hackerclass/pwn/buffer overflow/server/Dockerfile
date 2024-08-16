FROM alpine:latest
WORKDIR /
RUN echo "x86" > /etc/apk/arch \
    && apk add --no-cache socat libc6-compat
COPY . .
CMD socat TCP-L:1337,fork EXEC:"timeout 60s ./chall",reuseaddr,stderr
