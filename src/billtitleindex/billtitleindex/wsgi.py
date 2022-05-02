"""
WSGI config for billtitleindex project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""
import os

import django
from fastapi import FastAPI

# path to settings.py is defined in .env file
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "billtitleindex.billtitleindex.settings")
django.setup()


from billtitleindex.btiapp.endpoints import titles, utils  # noqa

app = FastAPI(
    title="BillTitleIndexAPI",
    description="API solution that provides titles information according to bills",
    version="v1.0",
)

app.include_router(titles.router, prefix="/api")
app.include_router(utils.router, prefix="/api")
