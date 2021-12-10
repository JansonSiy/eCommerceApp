from django.shortcuts import render

# STEP 3 - WRITE YOUR VIEWS

def store(request):
    # method + data
    context = {}#push it here
    return render(request, 'store/store.html', context)
    # Reference: https://docs.djangoproject.com/en/3.2/topics/http/shortcuts/
    # Request - The request object used to generate this response.
    # Template_name - The full name of a template to use or sequence of template names. If a sequence is given, the first template that exists will be used. See the template loading documentation for more information on how templates are found.
    # Context - A dictionary of values to add to the template context. By default, this is an empty dictionary. If a value in the dictionary is callable, the view will call it just before rendering the template.

def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)

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