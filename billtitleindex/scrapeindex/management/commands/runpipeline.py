from django.core.management.base import BaseCommand, CommandError
import logging

from scrapeindex import utils


class Command(BaseCommand):
    help = 'Run pipeline to load billstatus title data into PostgreSQL DB and index them.'
    
    def add_arguments(self, parser):
        parser.add_argument('bill_id', nargs='+', type=str)
        
    
    def handle(self, *args, **options):
        bill_id = options.get('bill_id', None)
        if bill_id:
            to_fetch = bill_id.split(",")
        else:
            to_fetch = utils.get_json_bills_to_process(options)
            
            if not to_fetch:
                logging.warn("All bills indexed.")
                return None
            
            limit = options.get('limit', None)
            if limit:
                to_fetch = to_fetch[:int(limit)]
        
        utils.process_set(to_fetch, options)