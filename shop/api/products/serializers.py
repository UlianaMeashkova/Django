from rest_framework import serializers

from products.models import Product


class ProductModelSerializer(serializers.HyperlinkedModelSerializer):

    has_image = serializers.SerializerMethodField()
    purchases_count = serializers.IntegerField(read_only=True)
    purchases_total = serializers.IntegerField(read_only=True)

    def get_has_image(self, obj: Product) -> bool:
        return bool(obj.image)

    class Meta:
        model = Product
        fields = [
            "id", "title", "has_image", "purchases_count", "purchases_total",
            "image", "color", "price", "created_at"
        ]