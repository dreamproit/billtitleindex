from decouple import config
from .base import *
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('PROD_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'billtitle',
        'USER': config('PROD_DB_USER'),
        'PASSWORD': config('PROD_DB_PWD'),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}