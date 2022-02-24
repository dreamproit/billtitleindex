from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

from scrapeindex.models import BillBasic, BillTitles, BillStageTitle


@registry.register_document
class BillBasicDocument(Document):
    """
        ### Bill basic information document
    """
    stage_titles = fields.NestedField(
        properties = {
            'title': fields.TextField(attr='title'),
            'titleNoYear': fields.TextField(attr='titleNoYear'),
            'type': fields.TextField(attr='type'),
            'As': fields.TextField(attr='As'),
            'is_for_portion': fields.BooleanField(attr='is_for_portion')
        }
    )
    class Index:
        name = 'bill-basic'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0
        }
        
    class Django:
        model = BillBasic
        fields = ['bill_id', 'bill_type', 'number', 'congress', 'introduced_at', 'updated_at']


@registry.register_document
class BillTitlesDocument(Document):
    """
        ### Bill titles document
    """
    bill_basic = fields.ObjectField(
        properties = {
            'bill_id': fields.TextField(attr='bill_id'),
            'bill_type': fields.TextField(attr='bill_type'),
            'number': fields.IntegerField(attr='number'),
            'congress': fields.IntegerField(attr='congress'),
            'introduced_at': fields.DateField(attr='introduced_at'),
            'updated_at': fields.DateField(attr='updated_at')
        }
    )
    
    class Index:
        name = 'bill-titles'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0
        }
    
    class Django:
        model = BillTitles
        fields = ['official_title', 'popular_title', 'short_title']
        related_models = [BillBasic]
        

@registry.register_document
class BillStageTitleDocument(Document):
    """ 
        ### Given stage titles document of each bill
    """
    bill_basic = fields.ObjectField(
        properties = {
            'bill_id': fields.TextField(attr='bill_id'),
            'bill_type': fields.TextField(attr='bill_type'),
            'number': fields.IntegerField(attr='number'),
            'congress': fields.IntegerField(attr='congress'),
            'introduced_at': fields.DateField(attr='introduced_at'),
            'updated_at': fields.DateField(attr='updated_at')
        }
    )
    
    class Index:
        name = 'bill-stage-title'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0
        }
        
    class Django:
        model = BillStageTitle
        fields = ['title', 'titleNoYear', 'type', 'As', 'is_for_portion']
        