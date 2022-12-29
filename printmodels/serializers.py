from rest_framework import serializers
from .models import PrintModel, SampleImage, DownloadableFile, Tag, PrintModelTag, Category, Order, Review, Payment


class PrintModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrintModel
        fields = ['name', 'description', 'price', 'download_file', 'owner']

class SampleImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SampleImage
        fields = ['print_model', 'image']

class DownloadableFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DownloadableFile
        fields = ['print_model', 'file']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']

class PrintModelTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrintModelTag
        fields = ['print_model', 'tag']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'print_models']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['user', 'print_models', 'total_price', 'order_date']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['print_model', 'user', 'rating', 'text']

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['order', 'payment_method', 'credit_card_number']