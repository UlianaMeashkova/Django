from rest_framework import viewsets


from api.products.serializers import ProductModelSerializer
from products.models import Product


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed.
    """

    queryset = Product.objects.all().order_by("-created_at")
    serializer_class = ProductModelSerializer
    permission_classes = []
