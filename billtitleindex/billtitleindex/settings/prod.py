from decouple import config
from .base import *
import os
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('PROD_SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('POSTGRES_DB'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': 'postgres',
        'PORT': '5432',
    }
}

ELASTICSEARCH_DSL={
    'default': {
        'hosts': 'es01:9200'
    },
}

# celery settings
CELERY_BROKER_URL = 'amqp://rabbitmq:5672'
CELERY_RESULT_BACKEND = 'amqp://rabbitmq:5672'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'