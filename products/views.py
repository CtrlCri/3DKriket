from rest_framework import viewsets
from .models import Category, Product, Purchase, Complaint
from .serializers import CategorySerializer, ProductSerializer, PurchaseSerializer, ComplaintSerializer

from rest_framework import permissions

class CategoryViewSet(viewsets.ModelViewSet):
    """
    Vista de categoria
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (permissions.IsAuthenticated,)

class ProductViewSet(viewsets.ModelViewSet):
    """
    Vista de producto
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (permissions.IsAuthenticated,)

class PurchaseViewSet(viewsets.ModelViewSet):
    """
    Vista de compra
    """
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    permission_classes = (permissions.IsAdminUser,)

class ComplaintViewSet(viewsets.ModelViewSet):
    """
    Vista de queja
    """
    queryset = Complaint.objects.all()
    serializer_class = ComplaintSerializer
    permission_classes = (permissions.IsAdminUser,)
