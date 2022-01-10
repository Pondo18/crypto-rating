# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
COPY requirements.txt /
RUN /usr/local/bin/python -m pip install --upgrade pip \
 && pip install -r requirements.txt
COPY crypto-rating /code
WORKDIR /code
CMD python manage.py runserver 0.0.0.0:8000