from dataclasses import fields
from itertools import product
from rest_framework import serializers
from .models import Product, Collection, Customer
from decimal import Decimal

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title', 'products_count']

    products_count = serializers.IntegerField()

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'slug', 'inventory',  'unit_price', 'price_with_tax', 'collection']
    price_with_tax = serializers.SerializerMethodField(method_name='Calculate_Tax')

    def Calculate_Tax(self, product: Product):
        return product.unit_price * Decimal(1.1)

class CustomerSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name =serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField(max_length=255)
    birth_date = serializers.DateField()
    membership = serializers.CharField(max_length=1)

class OrderSerializer(serializers.Serializer):
    placed_at = serializers.DateTimeField()
    payment_status = serializers.CharField(max_length=1)
    customer = CustomerSerializer()




