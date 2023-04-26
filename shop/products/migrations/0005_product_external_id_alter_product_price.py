# Generated by Django 4.1.7 on 2023-04-07 08:04

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='external_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=5, default=Decimal('0'), max_digits=10),
        ),
    ]