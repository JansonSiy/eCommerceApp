# STEP 4 - CREATE YOUR URLS FOR YOUR VIEWS
# When somebody requests a page from your website, Django will load the projectFolder_eCommerceApp.urls Python module because it’s pointed to by the ROOT_URLCONF setting.
# It finds the variable named urlpatterns and traverses the patterns in order.

from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout")
]