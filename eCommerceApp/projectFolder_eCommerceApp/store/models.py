# STEP 7 - CREATE YOUR MODELS
from django.db import models
#STEP 14 - CUSTOMIZE USER MODEL BY ASSOCIATING IT WITH PROFILE MODEL
from django.contrib.auth.models import User
from model_utils.fields import AutoCreatedField

# create migration files everytime you make changes in the models
# python manage.py makemigrations
# python manage.py migrate

# ORM bridges the gap between the code & the database
# import first - from store.models import *
# python manage.py shell - like a console
# from store.models import Profile - importing a model (ex. from appName.model.pyFile import className)
# Profile.objects.all() - show all objects
# profile = Profile() - creating an instance
# profile.name = "Jan" - adding data
# profile.save() - saving data
# Profile.objects.all()[0].name = "Jan" - example of calling a specific value

# class - we represent the model using a class
# Profile - we give it a name
# (models.Model) - in built in django, it's inheriting some basic functionality that all models will have
class Profile(models.Model):
    # STEP 14 - associating User and Profile model
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=100, null=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    created = AutoCreatedField()
    balance = models.IntegerField(default=0)
    # built in function that defines how a Profile is going to look in both admin and shell
    # self - instance of itself (instance of Profile)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    image = models.ImageField(null=True, blank=True)
    # blank attribute is False by default, since you set it to True, it will allow entry of an empty value
    description = models.TextField(default=False)

    def __str__(self):
        return self.name

class Order(models.Model):
    # reference - https://stackoverflow.com/questions/38388423/what-does-on-delete-do-on-django-models
    # https://stackoverflow.com/questions/26727616/not-null-constraint-failed-error
    user = models.ForeignKey(User, null=True, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, null=True, on_delete=models.DO_NOTHING)
    current_user = models.CharField(max_length=100, null=True)
    product_name = models.CharField(max_length=100, null=True)
    product_price = models.IntegerField(default=0, null=True)
    quantity = models.IntegerField(default=0, null=True)
    total_price = models.IntegerField(default=0, null=True)
    shipping_address = models.CharField(max_length=100, null=True)
    
    # reference - https://stackoverflow.com/questions/40618356/error-with-str-returned-non-string-type-int
    def __str__(self):
        return str(self.id)

# extra reference regarding .DateTimeField
# date_ordered = models.DateTimeField(auto_now_add=True)
# https://stackoverflow.com/questions/51389042/difference-between-auto-now-and-auto-now-add/51389274

class Type(models.Model):
    FOOD_TYPE = (
        ('vegtables', 'Vegetables'),
        ('meat_and_poultry', 'Meat and Poultry'),
        ('fish_and_seafood', 'Fish and Seafood'),
    )
    product_name = models.CharField(max_length=100, null=True)
    food_type = models.CharField(max_length=100, choices=FOOD_TYPE)