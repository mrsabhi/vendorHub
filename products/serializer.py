from rest_framework import serializers

from products.models import Products


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = [
            "id","vendor", "category", "product_name",
            "thumbnail", "price", "created_at", "updated_at"
        ]
