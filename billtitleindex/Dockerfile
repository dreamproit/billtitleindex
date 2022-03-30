#FROM python:3.8-slim-buster
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# install dependency.
#RUN apt-get -y update && apt-get -y --no-install-recommends install gcc && apt-get clean \
# && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /app
WORKDIR /app
COPY . .
# Install pip requirements
RUN pip install --no-cache-dir -r requirements.txt
