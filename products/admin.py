from django.contrib import admin
from products.models import *

admin.register(Product)
admin.register(Category)
admin.register(Purchase)
admin.register(Complaint)
