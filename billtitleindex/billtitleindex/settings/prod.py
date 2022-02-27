from decouple import config
from .base import *
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('PROD_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']