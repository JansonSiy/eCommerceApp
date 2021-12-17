from django.contrib import admin
# STEP 13 - ADD MODELS TO ADMIN
from .models import Profile, Product, Order

# Register your models here.
admin.site.register(Profile)
admin.site.register(Product)
admin.site.register(Order)