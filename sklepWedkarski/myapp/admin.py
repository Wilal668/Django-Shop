from django.contrib import admin
from .models import Item
from .models import Service

admin.site.register(Item)
admin.site.register(Service)