#FROM python:3.8-slim-buster
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

ENV POETRY_NO_INTERACTION=1
ENV POETRY_HOME=/opt/poetry
RUN pip install --no-cache-dir poetry==1.1.13 && \
    poetry config virtualenvs.create false && \
    mkdir -p /app

# install dependency.
#RUN apt-get -y update && apt-get -y --no-install-recommends install gcc && apt-get clean \
# && rm -rf /var/lib/apt/lists/*

WORKDIR /app
# Install pip requirements
COPY pyproject.toml poetry.lock ./

RUN poetry install --no-root

COPY ./src/billtitleindex/ .
#RUN pip install --no-cache-dir -r requirements.txt
