from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

from scrapeindex.models import BillBasic, BillTitles, BillStageTitle


@registry.register_document
class BillBasicDocument(Document):
    
    class Index:
        name = 'bill-basic'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0
        }
        
    class Django:
        model = BillBasic


@registry.register_document
class BillTitlesDocument(Document):
    
    class Index:
        name = 'bill-titles'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0
        }
    
    class Django:
        model = BillTitles
        

@registry.register_document
class BillStageTitleDocument(Document):
    
    class Index:
        name = 'bill-stage-title'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0
        }
        
    class Django:
        model = BillStageTitle
        