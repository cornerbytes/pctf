FROM python:alpine3.10

RUN adduser -D -u 1000 ctf

RUN apk --no-cache add socat

WORKDIR /home/ctf
COPY app.py ./
COPY templates/ ./templates/ 
RUN pip install flask
RUN pip install gunicorn
RUN chown -R ctf:root /home/ctf
RUN chmod 500 /home/ctf/app.py

USER ctf

CMD gunicorn -w 1 -b 0.0.0.0:8888 app:app
