# Generated by Django 4.1.7 on 2023-04-26 16:58

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0005_product_external_id_alter_product_price"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="price_usd",
            field=models.DecimalField(
                decimal_places=5, default=Decimal("0"), max_digits=10
            ),
        ),
    ]
