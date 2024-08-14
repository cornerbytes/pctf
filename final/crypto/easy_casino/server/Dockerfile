FROM python:alpine3.10

RUN adduser -D -u 1000 ctf

RUN apk --no-cache add socat

WORKDIR /home/ctf
COPY chall.py ./
RUN chmod 500 /home/ctf/chall.py
RUN chown -R ctf:root /home/ctf

USER ctf

CMD socat TCP-L:1337,fork EXEC:"timeout 60s python3 /home/ctf/chall.py",reuseaddr,stderr
