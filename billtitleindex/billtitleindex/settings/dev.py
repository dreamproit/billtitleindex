from decouple import config

from billtitleindex.settings.base import *  # noqa

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["localhost"]

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "billtitle",
        "USER": config("DEV_DB_USER"),
        "PASSWORD": config("DEV_DB_PWD"),
        "HOST": "localhost",
        "PORT": "5432",
    }
}

ELASTICSEARCH_DSL = {
    "default": {"hosts": "localhost:9200"},
}

# celery settings
CELERY_BROKER_URL = config("MESSAGE_BROKER_URI")
CELERY_RESULT_BACKEND = config("MESSAGE_BROKER_URI")
CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_TIMEZONE = "UTC"
