import os

from decouple import config

from billtitleindex.settings.base import *  # noqa


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY")

DEBUG = False

ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.environ.get("POSTGRES_DB"),
        "USER": os.environ.get("POSTGRES_USER"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
        "HOST": os.environ.get("POSTGRES_HOST"),
        "PORT": os.environ.get("POSTGRES_PORT"),
    }
}

ELASTICSEARCH_DSL = {
    "default": {"hosts": config("ELASTICSEARCH_URI")},
}

# celery settings
CELERY_BROKER_URL = config("MESSAGE_BROKER_URI")
CELERY_RESULT_BACKEND = config("MESSAGE_BROKER_URI")  # "amqp://rabbitmq:5672"
CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_TIMEZONE = "UTC"
