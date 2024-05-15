from rest_framework import serializers
from .models import Products

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['id', 'name', 'description', 'price', 'stock']

    def validate_stock(self, value):
        """
        Check that the stock is not negative
        """
        if value < 0:
            raise serializers.ValidationError("Stock must be positive")
        return value