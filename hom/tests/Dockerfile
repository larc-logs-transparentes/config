FROM python:3.12.2-bullseye

WORKDIR /app

COPY *.py /app/
COPY requirements.txt /app/
COPY *.bu /app/

RUN pip install --no-cache-dir -r requirements.txt

# Linha comentada para que o comando seja chamado pelo script do Jenkins
# Deste modo o output aparece nos logs do Jenkins
#CMD [ "pytest" ]