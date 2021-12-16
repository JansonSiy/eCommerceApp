# STEP 3 - WRITE YOUR VIEWS
from django.shortcuts import render
from .models import Profile
from .models import Product
from .models import Order
# STEP 11 - REQUIRE LOGIN AUTHENTICATION
from django.contrib.auth.decorators import login_required

def users(request):
    # Customer.objects.all().delete()
    
    # customerTwo = Customer(name='Jeff', age=28, gender='Male', email='jeff@example.com', address='San Diego City', status=False)
    # customerTwo.save()

    # customerThree = Customer(name='Jet', age=21, gender='Male', email='jet@example.com', address='Manila City', status=True)
    # customerThree.save()

    # customerFour = Customer(name='Joana', age=29, gender='Female', email='joana@example.com', address='Manila City', status=False)
    # customerFour.save()

    # customerFive = Customer(name='Janelle', age=33, gender='Female', email='janelle@example.com', address='Alabang City', status=True)
    # customerFive.save()

    # customerThree = Customer(name='Jason', age=35, gender='Male', email='jason@example.com', address='N/A', status=False)
    # customerThree.save()

    # users = Customer.objects.all()

    # context = {'users': users}

    context = {}

    return render(request, 'store/users.html', context)

def profile(request):
    # Customer.objects.all().delete()

    # customerOne = Customer(name='Jan', age=27, gender='Male', address='Pasig City', status=True)
    # customerOne.save()

    # context = {'customer': customerOne, 'user': current_user}

    current_user = request.user

    context = {'user': current_user}

    return render(request, 'store/profile.html', context)

# STEP 11 - REQUIRE LOGIN AUTHENTICATION
@login_required(login_url='/login')
def mystore(request):
    Product.objects.all().delete()

    productOne = Product(name='Apple', price=10, image='https://media.istockphoto.com/vectors/simple-apple-in-flat-style-vector-illustration-vector-id1141529240?k=20&m=1141529240&s=612x612&w=0&h=_j9z-sPT6AqFDSSXHnSYWrXOvDOgyMmSdTUrBiZULCo=')
    productOne.save()

    productTwo = Product(name='Banana', price=20, image='https://media.istockphoto.com/vectors/banana-icon-fresh-banana-on-white-vector-id871892360?k=20&m=871892360&s=170667a&w=0&h=taOnjSKzU2ZHmYZu0-pfM9v5zueodjH4y0rw6xwe9-M=')
    productTwo.save()

    productThree = Product(name='Mango', price=30, image='https://media.istockphoto.com/vectors/mango-ripe-fruit-simple-isolated-on-white-background-yellow-mango-vector-id1251708686?k=20&m=1251708686&s=170667a&w=0&h=QWEYqI84yNHY-_eMwzRloBhKnVmbYk4azADujwJAXuU=')
    productThree.save()

    productFour = Product(name='Grapes', price=40, image='https://media.istockphoto.com/vectors/grapes-icon-vector-id1193509529?k=20&m=1193509529&s=612x612&w=0&h=ZfW6iDjfFsiylUsMAEq4o_YQuJ7GdjivbE_g30VENaE=')
    productFour.save()

    productFive = Product(name='Watermelon', price=50, image='https://t4.ftcdn.net/jpg/02/71/31/29/360_F_271312913_fNkJIq7J4EojJTfB4flj6NLvl1NjYPJ4.jpg')
    productFive.save()

    productSix = Product(name='Dragon Fruit', price=60, image='https://media.istockphoto.com/vectors/whole-and-halved-dragonfruit-pitaya-isolated-on-white-background-vector-id1264977960?b=1&k=20&m=1264977960&s=612x612&w=0&h=p64_CCtRkJLzMU7tcp0KMUwQHFF5G6_vkHrWmmAJ_n4=')
    productSix.save()

    products = Product.objects.all()
    
    current_user = request.user

    context = {'products': products, 'user': current_user}

    return render(request, 'store/mystore.html', context)
    # reference: https://docs.djangoproject.com/en/3.2/topics/http/shortcuts/
    # request - The request object used to generate this response.
    # template_name - The full name of a template to use or sequence of template names. If a sequence is given, the first template that exists will be used. See the template loading documentation for more information on how templates are found.
    # context - A dictionary of values to add to the template context. By default, this is an empty dictionary. If a value in the dictionary is callable, the view will call it just before rendering the template.

def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)

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