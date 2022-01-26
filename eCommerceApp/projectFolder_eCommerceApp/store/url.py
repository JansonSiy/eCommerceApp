# STEP 4 - CREATE YOUR URLS FOR YOUR VIEWS
# When somebody requests a page from your website, Django will load the projectFolder_eCommerceApp.urls Python module because it’s pointed to by the ROOT_URLCONF setting.
# It finds the variable named urlpatterns and traverses the patterns in order.

from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    # User model
    path('users/', views.users, name='users'),
    path('exportUsers/', views.exportUsers, name='exportUsers'),
    # Profile model
    path('profile/', views.profile, name='profile'),
    path('<int:user_id>/activate/', views.activate, name='activate'),
    # Product model
    path('mystore/', views.mystore, name='mystore'),
    path('<int:product_id>/details/', views.details, name='details'),
    path('filter/', views.filter, name='filter'),
    path('exportProducts/', views.exportProducts, name='exportProducts'),
    # Order model
    path('cart/', views.cart, name='cart'),
    path('<int:product_id>/addToCart/', views.addToCart, name='addToCart'),
    path('<int:order_id>/checkout/', views.checkout, name='checkout')
]