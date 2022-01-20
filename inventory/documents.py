from django.db.models import fields
from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registeries import registry

from .models import ProductInventory

@registry.register_document
class ProductInventoryDocment(Document):

    class Index:
        name = "productinventory"

    
    class Django:
        model = ProductInventory
        fields = ["id", "sku",]