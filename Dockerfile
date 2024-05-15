FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apt-get update \
    && apt-get install -y libpq-dev gcc \
    && apt-get clean

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY . /app