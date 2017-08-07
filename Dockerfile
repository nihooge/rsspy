FROM python:latest

COPY requirements.txt /

RUN pip install -r ./requirements.txt

COPY app/ /app/

WORKDIR /app

ENV FLASK_APP=rss.py
CMD flask run -h 0.0.0.0 -p 5000 