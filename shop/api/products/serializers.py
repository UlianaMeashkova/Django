from rest_framework import serializers
from rest_framework.exceptions import ValidationError

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

    def __init__(self, data, *args, **kwargs):
        super().__init__(data, *args, **kwargs)

        if data is not None:
            self.initial_data = data

        self._validated_data = {}
        self._errors = {}

    def to_internal_value(self, data: dict = None) -> dict:
        result = {}
        for field in data:
            primitive_value = field.get_value(data)
            validated_value = field.run_validation(primitive_value)
            result[field.source_attrs] = validated_value
        return result

    def validate(self, data: dict = None):
        return data

    def run_validation(self, data: dict = None) -> dict:
        value = self.to_internal_value(data)
        return self.validate(value)

    def is_valid(self, raise_exception: bool = False):
        try:
            self._validated_data = self.run_validation(self.initial_data)
        except ValidationError as exc:
            self._validated_data = {}
            self._errors = exc.detail
        else:
            self._errors = {}

        if self._errors and raise_exception:
            raise ValidationError(self.errors)

        return not bool(self._errors)