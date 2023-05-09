from decimal import Decimal

import factory

from factory.django import DjangoModelFactory

from products.models import Product


class ProductFactory(DjangoModelFactory):
    class Meta:
        model = Product

    title = factory.Faker("word")
    color = "RED"
    price = Decimal(100)
    price_usd = Decimal(290)