FROM python:3.8-slim-buster

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# install dependency
RUN apt-get -y update
RUN apt-get -y install gcc git

RUN mkdir -p /app
WORKDIR /app
COPY . .

RUN mv wait-for /bin/wait-for
CMD ["chmod", "+x", "/bin/wait-for"]

# Install pip requirements
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# EXPOSE 8080

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]