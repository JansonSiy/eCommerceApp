from django.contrib import admin
from .models import Customer, Product, Order
# STEP 13 - ADD MODELS TO ADMIN

# Register your models here.
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)