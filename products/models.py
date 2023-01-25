from django.db import models
from base.models import BaseModel
from users.models import User

class Category(BaseModel):
    """
    Modelo de categoria
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Product(BaseModel):
    """
    Modelo de producto
    """
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Purchase(BaseModel):
    """
    Modelo de compra
    """
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Purchase by {self.customer.name} for product {self.product.name}"

class Complaint(BaseModel):
    """
    Modelo de queja
    """
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    complaint_category = models.CharField(max_length=255)
    description = models.TextField()
    resolution = models.TextField()

    def __str__(self):
        return f"Complaint by {self.purchase.customer.name} for purchase {self.purchase.id}"

