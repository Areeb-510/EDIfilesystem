# Generated by Django 4.2.2 on 2023-06-19 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PurchaseOrder",
            fields=[
                ("sender", models.CharField(max_length=100, null=True)),
                ("receiver", models.CharField(max_length=100, null=True)),
                (
                    "purchaseOrderNumber",
                    models.CharField(max_length=100, primary_key=True, serialize=False),
                ),
                ("date", models.DateField()),
            ],
        ),
    ]
