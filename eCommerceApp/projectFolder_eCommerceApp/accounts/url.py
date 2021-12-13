# STEP 8 - CREATE ACCOUNTS APP
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup')
]