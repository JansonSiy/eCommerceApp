# STEP 7 - CREATE YOUR MODELS
from django.db import models

# CREATE MIGRATION FILES (everytime you make changes in the models)
# python manage.py makemigrations
# MIGRATING
# python manage.py migrate

# class - we represent the model using a class
# Customer - we give it a name
# (models.Model) - in built in django, it's inheriting some basic functionality that all models will have
class Customer(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    status = models.BooleanField(default=True)

# ORM bridges the gap between the code & the database
# import first - from store.models import *
# python mange.py shell - like a console
# from store.models import Customer - importing a model (ex. from appName.model.pyFile import className)
# Customer.objects.all() - show all objects
# customer = Customer() - creating an instance
# customer.name = "Jan" - adding data
# customer.save() - saving data
# Customer.objects.all()[0].name = "Jan" - example of calling a specific value

# built in function that defines how a Customer is going to look in both admin and shell
# self - instance of itself (instance of Customer)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    image = models.ImageField(null=True, blank=True)
    # blank attribute is False by default, since you set it to True, it will allow entry of an empty value

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    # reference - https://stackoverflow.com/questions/38388423/what-does-on-delete-do-on-django-models
    quantity = models.IntegerField(default=0)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.id

# EXTRA REFERENCE
# date_ordered = models.DateTimeField(auto_now_add=True)
# reference - https://stackoverflow.com/questions/51389042/difference-between-auto-now-and-auto-now-add/51389274