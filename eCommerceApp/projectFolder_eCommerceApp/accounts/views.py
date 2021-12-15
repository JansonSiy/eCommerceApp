from typing import ContextManager
from django.shortcuts import render, redirect
# also import redirect

# STEP 9 - USER CREATION FORM
# STEP 10 - AUTHENTICATION FORM
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# UserCreationForm is used for creating a new user that can use our web application
# AuthenticationForm is used to log users in

from django.contrib.auth import login, logout
# importing login function

def signup_view(request):
    # if it's a post request
    if request.method == 'POST':
        # passing all the values/data of the post request to a new instance
        form = UserCreationForm(request.POST)
        # if the form is valid (follows the instructions imbeded in django form) it saves the data
        # .is_valid() is a built in method that can check that, that returns boolean value
        if form.is_valid():
            # storing it to a variable after saving
            user = form.save()
            # login the user after
            login(request, user)
            # then redirect('appNameInUrl.py:urlName')
            return redirect('store:mystore')
    else:
        form = UserCreationForm()
        # creating a new instance (then send it over to the template)
    
    context = {'form': form}
    
    return render(request, 'accounts/signup.html', context)

def login_view(request):
    if request.method == 'POST':
        # pass the data here for validation, data is equals to request.POST, this is the syntax for this parameter
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log in the user using .get_user()
            user = form.get_user()
            # then use the login method and pass 2 parameters, the request and the user details
            login(request, user)
            return redirect('store:mystore')
    else:
        form = AuthenticationForm()
    
    context = {'form': form}

    return render(request, 'accounts/login.html', context)

def logout_view(request):
    # best practice is to use post request for logout not get
    if request.method == 'POST':
        # django already knows which user is logged in so no need to specify in the parameter
        logout(request)
        return redirect('accounts:logout_page')

def logout_page(request):
    context = {}
    return render(request, 'accounts/logout_page.html', context)