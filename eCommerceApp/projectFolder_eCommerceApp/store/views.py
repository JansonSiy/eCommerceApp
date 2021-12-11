# STEP 3 - WRITE YOUR VIEWS
from django.shortcuts import render
from .models import Customer
from .models import Product
from .models import Order

def profile(request):
    # customerOneGender = customerOne.gender

    # if customerOneGender == True:
    #     customerOneGender = 'Male'
    # else:
    #     customerOneGender = 'Female'
    #     customerOne.save()

    Customer.objects.all().delete()

    customerOne = Customer(name='Jan', age=27, gender=True, email='jan@example.com', address='Pasig City')
    customerOne.save()

    context = {'customer': customerOne}

    return render(request, 'store/profile.html', context)

def store(request):
    Product.objects.all().delete()

    productOne = Product(name='Apple', price=10, image='https://media.istockphoto.com/vectors/simple-apple-in-flat-style-vector-illustration-vector-id1141529240?k=20&m=1141529240&s=612x612&w=0&h=_j9z-sPT6AqFDSSXHnSYWrXOvDOgyMmSdTUrBiZULCo=')
    productOne.save()

    productTwo = Product(name='Banana', price=20, image='https://webstockreview.net/images/banana-clipart-simple-5.png')
    productTwo.save()

    productThree = Product(name='Mango', price=30, image='https://media.istockphoto.com/vectors/mango-ripe-fruit-simple-isolated-on-white-background-yellow-mango-vector-id1251708686?k=20&m=1251708686&s=170667a&w=0&h=QWEYqI84yNHY-_eMwzRloBhKnVmbYk4azADujwJAXuU=')
    productThree.save()

    productFour = Product(name='Grapes', price=40, image='https://t4.ftcdn.net/jpg/02/26/62/03/360_F_226620346_fjIT0VVzhnGhSp9rjLhSyw76AqNNRGnx.jpg')
    productFour.save()

    productFive = Product(name='Watermelon', price=50, image='https://t4.ftcdn.net/jpg/02/71/31/29/360_F_271312913_fNkJIq7J4EojJTfB4flj6NLvl1NjYPJ4.jpg')
    productFive.save()

    productSix = Product(name='Dragon Fruit', price=60, image='https://media.istockphoto.com/vectors/whole-and-halved-dragonfruit-pitaya-isolated-on-white-background-vector-id1264977960?b=1&k=20&m=1264977960&s=612x612&w=0&h=p64_CCtRkJLzMU7tcp0KMUwQHFF5G6_vkHrWmmAJ_n4=')
    productSix.save()

    products = Product.objects.all()
    
    context = {'products': products}

    return render(request, 'store/store.html', context)
    # reference: https://docs.djangoproject.com/en/3.2/topics/http/shortcuts/
    # request - The request object used to generate this response.
    # template_name - The full name of a template to use or sequence of template names. If a sequence is given, the first template that exists will be used. See the template loading documentation for more information on how templates are found.
    # context - A dictionary of values to add to the template context. By default, this is an empty dictionary. If a value in the dictionary is callable, the view will call it just before rendering the template.

def order(request):

    context = {}
    return render(request, 'store/order.html', context)

# shorthand - please note that your templates should not be in a store folder
# from django.shortcuts import render_template

# def store(request):
#     context = {}
#     return render_template('store.html')

# def cart(request):
#     context = {}
#     return render_template('cart.html')

# def checkout(request):
#     context = {}
#     return render_template('checkout.html')