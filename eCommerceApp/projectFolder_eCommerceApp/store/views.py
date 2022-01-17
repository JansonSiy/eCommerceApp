# STEP 3 - WRITE YOUR VIEWS
from django.shortcuts import render, redirect
from .models import User, Profile, Product, Order
# STEP 11 - REQUIRE LOGIN AUTHENTICATION
from django.contrib.auth.decorators import login_required
from .filters import ProductFilter

# reference: https://docs.djangoproject.com/en/3.2/topics/http/shortcuts/
# request - The request object used to generate this response.
# template_name - The full name of a template to use or sequence of template names. If a sequence is given, the first template that exists will be used. See the template loading documentation for more information on how templates are found.
# context - A dictionary of values to add to the template context. By default, this is an empty dictionary. If a value in the dictionary is callable, the view will call it just before rendering the template.

# def users(request, profile_id):
def users(request):
    current_user = request.user
    users = User.objects.all()
    # profile = Profile.objects.get(pk=profile_id)

    context = {'current_user': current_user, 'users': users }
    # context = {'current_user': current_user, 'users': users, 'profile': profile }
    
    return render(request, 'store/users.html', context)

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

def profile(request):
    current_user = request.user
    myOrders = Order.objects.filter(current_user=current_user)
    orderCount = Order.objects.filter(current_user=current_user).count()

    context = {'current_user': current_user, 'myOrders': myOrders, 'orderCount': orderCount}

    return render(request, 'store/profile.html', context)

# Customer.objects.all().delete()

# customerOne = Customer(name='Jan', age=27, gender='Male', address='Pasig City', status=True)
# customerOne.save()

# context = {'customer': customerOne, 'user': current_user}

# STEP 11 - REQUIRE LOGIN AUTHENTICATION
@login_required(login_url='/login')
def mystore(request):
    current_user = request.user
    products = Product.objects.all()

    context = {'current_user': current_user, 'products': products}

    return render(request, 'store/mystore.html', context)

# Product.objects.all().delete()

# productOne = Product(name='Apple', price=10, quantity=5, image='https://media.istockphoto.com/vectors/simple-apple-in-flat-style-vector-illustration-vector-id1141529240?k=20&m=1141529240&s=612x612&w=0&h=_j9z-sPT6AqFDSSXHnSYWrXOvDOgyMmSdTUrBiZULCo=', description=)
# productOne.save()
# productTwo = Product(name='Banana', price=20, quantity=3, image='https://media.istockphoto.com/vectors/banana-icon-fresh-banana-on-white-vector-id871892360?k=20&m=871892360&s=170667a&w=0&h=taOnjSKzU2ZHmYZu0-pfM9v5zueodjH4y0rw6xwe9-M=', description=)
# productTwo.save()
# productThree = Product(name='Mango', price=30, quantity=1, image='https://media.istockphoto.com/vectors/mango-ripe-fruit-simple-isolated-on-white-background-yellow-mango-vector-id1251708686?k=20&m=1251708686&s=170667a&w=0&h=QWEYqI84yNHY-_eMwzRloBhKnVmbYk4azADujwJAXuU=', description=)
# productThree.save()
# productFour = Product(name='Grapes', price=40, quantity=6, image='https://media.istockphoto.com/vectors/grapes-icon-vector-id1193509529?k=20&m=1193509529&s=612x612&w=0&h=ZfW6iDjfFsiylUsMAEq4o_YQuJ7GdjivbE_g30VENaE=', description=)
# productFour.save()
# productFive = Product(name='Watermelon', price=50, quantity=4, image='https://t4.ftcdn.net/jpg/02/71/31/29/360_F_271312913_fNkJIq7J4EojJTfB4flj6NLvl1NjYPJ4.jpg', description=)
# productFive.save()
# productSix = Product(name='Dragon Fruit', price=60, quantity=2, image='https://media.istockphoto.com/vectors/whole-and-halved-dragonfruit-pitaya-isolated-on-white-background-vector-id1264977960?b=1&k=20&m=1264977960&s=612x612&w=0&h=p64_CCtRkJLzMU7tcp0KMUwQHFF5G6_vkHrWmmAJ_n4=', description=)
# productSix.save()

def cart(request):
    current_user = request.user
    myOrders = Order.objects.filter(current_user=current_user)
    orderCount = Order.objects.filter(current_user=current_user).count()

    context = {'current_user': current_user, 'myOrders': myOrders, 'orderCount': orderCount}

    return render(request, 'store/cart.html', context)

def details(request, product_id):
    current_user = request.user
    product = Product.objects.get(pk=product_id)

    context = {'current_user': current_user, 'product': product}

    return render(request, 'store/details.html', context)

def addToCart(request, product_id):
    current_user = request.user
    product = Product.objects.get(pk=product_id)
    total_price = product.price * 1
 
    Order.objects.create(current_user=current_user, product_name=product.name, product_price=product.price, quantity=1, total_price=total_price, shipping_address=current_user.profile.address)

    currentOrder = Order.objects.last()

    context = {'current_user': current_user, 'product': product, 'order': currentOrder}

    return render(request, 'store/addToCart.html', context)

def activate(request, user_id):
    current_user = request.user
    user = User.objects.get(pk=user_id)

    # associated model (you need to do this)
    userProfile = user.profile

    if userProfile.status == False:
        userProfile.status = True
        userProfile.save()
    else:
        userProfile.status = False
        userProfile.save()

    context = {'current_user': current_user, 'user': user}

    return render(request, 'store/activate.html', context)

def checkout(request, order_id):
    current_user = request.user
    order = Order.objects.get(pk=order_id)
    
    # quantity of an order is 1 (by default)
    orderQuantity = order.quantity

    # targeting the product
    product = Product.objects.get(name=order.product_name)

    # getting the quantity of the product = 5
    productQuantity = product.quantity

    # 5 - 1 = 4
    newProductQuantity = productQuantity - orderQuantity
    product.quantity = newProductQuantity
    product.save()

    context = {'current_user': current_user, 'order': order}

    return render(request, 'store/checkout.html', context)

def filter(request):
    products = Product.objects.all()
    filter = ProductFilter(request.GET, queryset = products)

    context = {'filter': filter}

    return render(request, 'store/filter.html', context)

# shorthand for template rendering - from django.shortcuts import render_template
# def store(request):
#     context = {}
#     return render_template('store.html')