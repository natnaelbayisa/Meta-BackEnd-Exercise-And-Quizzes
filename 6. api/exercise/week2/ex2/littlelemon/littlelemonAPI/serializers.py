from rest_framework import serializers
from .models import MenuItem
from decimal import Decimal

class MenuItemSerializer(serializers.ModelSerializer):
    stock = serializers.IntegerField(source ="inventory")
    price_after_tax = serializers.SerializerMethodField(method_name='calculate_tax')

    class Meta:
        model = MenuItem
        # inventory is replaced by stock but it doesn't changed from the model
        fields = ['id', 'title', 'price', 'stock', 'price_after_tax']

    def calculate_tax(self, product:MenuItem):
        return product.price * Decimal(1.1)

# selective output
class MenuItemSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    price = serializers.DecimalField(max_digits=6, decimal_places=2)
    inventory = serializers.IntegerField()