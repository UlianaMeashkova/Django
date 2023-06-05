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
            "id",
            "title",
            "has_image",
            "purchases_count",
            "purchases_total",
            "image",
            "color",
            "price",
            "created_at",
        ]


class ProductSerializer(serializers.Serializer):
    external_id = serializers.CharField(
        max_length=255, allow_blank=True, allow_null=True
    )
    title = serializers.CharField(max_length=255)
    image = serializers.ImageField(allow_empty_file=True)
    color = serializers.CharField(max_length=32)
    price = serializers.DecimalField(decimal_places=5, max_digits=10)
    price_usd = serializers.DecimalField(decimal_places=5, max_digits=10)
    excerpt = serializers.CharField(allow_blank=True, allow_null=True)
    description = serializers.CharField(allow_blank=True, allow_null=True)
    created_at = serializers.DateTimeField()
    purchases_total = serializers.DecimalField(decimal_places=5, max_digits=10)
