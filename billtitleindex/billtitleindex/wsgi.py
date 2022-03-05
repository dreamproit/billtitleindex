"""
WSGI config for billtitleindex project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from fastapi import FastAPI

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'billtitleindex.settings')

application = get_wsgi_application()

from btiapp.urls import router as main_router

app = FastAPI(
    title="BillTitleIndexAPI",
    description="API solution that provides titles information according to bills",
    version="v1.0"
)

app.include_router(main_router, prefix="/api")

