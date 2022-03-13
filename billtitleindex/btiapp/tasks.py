# tasks
from __future__ import absolute_import, unicode_literals
from django.core.management import call_command
from celery.utils.log import get_task_logger
from celery import shared_task
import subprocess     

# logging
logger = get_task_logger(__name__)


# scraping function
@shared_task
def scrape_bills():
    working_directory = ''
    scraping_process = subprocess.Popen(['usc-run', 'govinfo', '--bulkdata=BILLSTATUS'], cwd=working_directory)
    if not scraping_process.poll() is None:
        # process has finished
        converting_process = subprocess.Popen(['usc-run', 'bills'])
        

# pipeline function
@shared_task()
def run_pipeline():
    call_command('runpipeline', verbosity=3, interactive=False)
    
        
    

