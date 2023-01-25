from rest_framework import serializers
from .models import Category, Product, Purchase, Complaint


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializador de categoria
    """
    class Meta:
        model = Category
        fields = ('id', 'name', 'created_at', 'updated_at')

class ProductSerializer(serializers.ModelSerializer):
    """
    Serializador de producto
    """
    category = CategorySerializer(read_only=True)
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'stock', 'category', 'created_at', 'updated_at')

class PurchaseSerializer(serializers.ModelSerializer):
    """
    Serializador de compra
    """
    customer = serializers.StringRelatedField()
    product = ProductSerializer(read_only=True)
    class Meta:
        model = Purchase
        fields = ('id', 'customer', 'product', 'quantity', 'total_price', 'created_at', 'updated_at')

class ComplaintSerializer(serializers.ModelSerializer):
    """
    Serializador de queja
    """
    purchase = PurchaseSerializer(read_only=True)
    class Meta:
        model = Complaint
        fields = ('id', 'purchase', 'complaint_category', 'description', 'resolution', 'created_at', 'updated_at')
