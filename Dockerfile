FROM python:3.8

RUN mkdir /app

WORKDIR /app

COPY main.py .

EXPOSE 0000