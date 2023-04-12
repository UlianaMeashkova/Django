from django.db.models import Count, Sum
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
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


class ProductViewFullSet(ListAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
    paginator_class = PageNumberPagination
    permission_classes = []

    def get_queryset(self):
        return self.queryset.all()

    def get_serializer(self, *args, **kwargs):
        return self.serializer_class(*args, **kwargs)

    def get_paginator(self, *args, **kwargs):
        return self.paginator_class()

    def paginate_queryset(self, queryset):
        return self.get_paginator().paginate_queryset(queryset, self.request, view=self)

    def get_paginated_response(self, data):
        return self.get_paginator().get_paginated_response(data)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
