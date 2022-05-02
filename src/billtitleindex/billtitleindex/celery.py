from __future__ import absolute_import

import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "billtitleindex.billtitleindex.settings"
)

app = Celery("billtitleindex")

app.conf.timezone = "UTC"

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()

app.conf.beat_schedule = {
    "scraping-task-midnight-daily": {
        "task": "billtitleindex.btiapp.tasks.scrape_bills",
        "schedule": crontab(hour=0, minute=0),
    },
    "pipeline-task-everyday-4am": {
        "task": "billtitleindex.btiapp.tasks.run_pipeline",
        "schedule": crontab(hour=4, minute=0),
    },
}
