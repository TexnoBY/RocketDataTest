# syntax=docker/dockerfile:1
FROM python:3.9-alpine

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install psycopg2


WORKDIR /code
COPY requirements.txt /code/


RUN pip install -r requirements.txt



COPY . /code/