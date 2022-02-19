# tasks
from __future__ import absolute_import, unicode_literals
from webbrowser import get
from celery import Celery
from celery import app, shared_task


# job model
from .models import BillStageTitle

# scraping
import requests
import json
from datetime import datetime
import lxml

# logging
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


# save function
@shared_task()
def run_pipeline():
    return

# scraping function
@shared_task
def scrape_bills():
    return

