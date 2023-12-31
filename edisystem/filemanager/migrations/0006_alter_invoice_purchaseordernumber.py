# Generated by Django 4.2.2 on 2023-06-19 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("filemanager", "0005_remove_invoice_date_remove_invoice_receiver_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="invoice",
            name="purchaseOrderNumber",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                primary_key=True,
                serialize=False,
                to="filemanager.purchaseorder",
                unique=True,
            ),
        ),
    ]
