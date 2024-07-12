FROM python:3.12.2-bullseye

WORKDIR /app

COPY *.py /app/
COPY requirements.txt /app/
COPY *.bu /app/

RUN pip install --no-cache-dir --upgrade -r requirements.txt
