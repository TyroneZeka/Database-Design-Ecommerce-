from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductInventory)
admin.site.register(Media)
admin.site.register(Brand)
admin.site.register(ProductAttribute)
admin.site.register(ProductTypeAttribute)
admin.site.register(ProductAttributeValues)
admin.site.register(ProductAttributeValue)
