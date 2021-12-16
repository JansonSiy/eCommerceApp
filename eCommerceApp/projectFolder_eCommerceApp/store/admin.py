from django.contrib import admin
from .models import Profile, Product, Order
# STEP 13 - ADD MODELS TO ADMIN

# Register your models here.
admin.site.register(Profile)
admin.site.register(Product)
admin.site.register(Order)