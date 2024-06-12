FROM python:3.11.0-alpine
LABEL authors="0gl04q"

WORKDIR /usr/src/storage

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

USER root

RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/storage
RUN pip install -r requirements.txt

COPY . /usr/src/storage

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]