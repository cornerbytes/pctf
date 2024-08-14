FROM python:alpine3.10
RUN apk add --no-cache figlet \
    && pip3 install flask \
    && adduser -s /bin/bash -D ctf

USER ctf
WORKDIR /opt/teks\ keren
COPY . .

CMD ["python3", "main.py"]
