# tasks
from __future__ import absolute_import, unicode_literals
from webbrowser import get
from celery import Celery
from celery import app, shared_task


from django.core.management import call_command
import subprocess     

# logging
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


# scraping function
@shared_task
def scrape_bills():
    scraping_process = subprocess.Popen(['usc-run', 'govinfo', '--bulkdata=BILLSTATUS'])
    if not scraping_process.poll() is None:
        # process has finished
        converting_process = subprocess.Popen(['usc-run', 'bills'])
        

# pipeline function
@shared_task()
def run_pipeline():
    call_command('runpipeline', verbosity=3, interactive=False)
    
        
    

