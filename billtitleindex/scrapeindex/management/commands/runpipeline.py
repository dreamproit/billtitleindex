from lib2to3.pytree import Base
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

class Command(BaseCommand):
    help = 'Run pipeline to load bill title data into PostgreSQL DB and index them.'
    
    def add_arguments(self, parser):
        return super().add_arguments(parser)
    
    def handle(self, *args, **options):
        return super().handle(*args, **options)