from django.db.models import Count, Sum
from rest_framework import viewsets


from django.db.models import Count, Sum
from rest_framework import viewsets
from rest_framework.response import Response

from api.products.serializers import ProductModelSerializer
from products.models import Product


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed.
    """

    queryset = Product.objects.annotate(
        purchases_count=Count("purchases")
    ).annotate(
        purchases_total=Sum("purchases__count")
    ).order_by("-created_at")

    serializer_class = ProductModelSerializer
    permission_classes = []
