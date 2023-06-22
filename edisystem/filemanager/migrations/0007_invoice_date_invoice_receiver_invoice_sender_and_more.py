# Generated by Django 4.2.2 on 2023-06-19 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("filemanager", "0006_alter_invoice_purchaseordernumber"),
    ]

    operations = [
        migrations.AddField(
            model_name="invoice",
            name="date",
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name="invoice",
            name="receiver",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="invoice",
            name="sender",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="invoice",
            name="purchaseOrderNumber",
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]