from rest_framework import serializers
from .models import Inventory
from apps.products.models import Products


class InventorySerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Products.objects.all(), source='product', write_only=True)

    class Meta:
        model = Inventory
        fields = ['id', 'product', 'product_id', 'quantity', 'type', 'date']
