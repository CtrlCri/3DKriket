from rest_framework import viewsets
from .serializers import PrintModelSerializer, SampleImageSerializer, DownloadableFileSerializer, TagSerializer, PrintModelTagSerializer, CategorySerializer, OrderSerializer, ReviewSerializer, PaymentSerializer

from .models import PrintModel, SampleImage, DownloadableFile, Tag, PrintModelTag, Category, Order, Review, Payment


class PrintModelViewSet(viewsets.ModelViewSet):
    queryset = PrintModel.objects.all()
    serializer_class = PrintModelSerializer

class SampleImageViewSet(viewsets.ModelViewSet):
    queryset = SampleImage.objects.all()
    serializer_class = SampleImageSerializer

class DownloadableFileViewSet(viewsets.ModelViewSet):
    queryset = DownloadableFile.objects.all()
    serializer_class = DownloadableFileSerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class PrintModelTagViewSet(viewsets.ModelViewSet):
    queryset = PrintModelTag.objects.all()
    serializer_class = PrintModelTagSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer