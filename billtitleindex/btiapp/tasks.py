# tasks
from __future__ import absolute_import
from __future__ import unicode_literals

import os
import subprocess

from celery.utils.log import get_task_logger
from django.core.management import call_command

from billtitleindex.celery import app
from btiapp import utils

# logging
logger = get_task_logger(__name__)


# scraping function
@app.task
def scrape_bills():
    print("start scraping...")
    working_directory = os.path.abspath(os.path.join(utils.get_data_path(), "../"))
    print(working_directory)
    scraping_process = subprocess.Popen(
        ["usc-run", "govinfo", "--bulkdata=BILLSTATUS"], cwd=working_directory
    )
    if not scraping_process.poll() is None:
        # process has finished
        subprocess.Popen(["usc-run", "bills"], cwd=working_directory)


# pipeline function
@app.task
def run_pipeline():
    call_command("runpipeline", verbosity=3)
