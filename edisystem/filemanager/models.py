from django.db import models

# Create your models here.


class PurchaseOrder(models.Model):
    sender = models.CharField(max_length=100,null=True)
    receiver = models.CharField(max_length=100,null=True)
    purchaseOrderNumber = models.IntegerField(primary_key=True,null=False)
    date = models.DateField()
    edi_type = models.CharField(null=False,default='850')

    def __str__(self):
        return str(self.purchaseOrderNumber)


class Invoice(models.Model):
    sender = models.CharField(max_length=100,null=True)
    receiver = models.CharField(max_length=100,null=True)
    purchaseOrderNumber = models.IntegerField(primary_key=True,null=False)
    date = models.DateField(null=True)
    edi_type = models.CharField(null=False,default='810')

    def __str__(self):
        return str(self.purchaseOrderNumber)

