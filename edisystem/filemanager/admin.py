from django.contrib import admin
from .models import Invoice,PurchaseOrder

# Register your models here.


admin.site.register(PurchaseOrder)
admin.site.register(Invoice)