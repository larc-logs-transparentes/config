FROM python:3.12.2-slim-bullseye

WORKDIR /app

COPY *.py /app/
COPY requirements.txt /app/
COPY bus /app/bus

RUN pip install --no-cache-dir --upgrade -r requirements.txt
