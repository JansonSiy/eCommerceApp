from typing import ContextManager
from django.shortcuts import render, redirect
# also import redirect

# STEP 9 - USER CREATION FORM
# STEP 10 - AUTHENTICATION FORM
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# UserCreationForm is used for creating a new user that can use our web application
# AuthenticationForm is used to log users in

from django.contrib.auth import login
# importing login function

def signup_view(request):
    # if it's a post request
    if request.method =='POST':
        # passing all the values/data of the post request to a new instance
        postReqForm = UserCreationForm(request.POST)
        # if the form is valid (follows the instructions imbeded in django form) it saves the data
        # .is_valid() is a built in method that can check that, that returns boolean value
        if postReqForm.is_valid():
            # storing it to a variable after saving
            userFromSignup = postReqForm.save()
            # login the user after
            login(request, userFromSignup)
            # then redirect('appNameInUrl.py:urlName')
            return redirect('store:mystore')
    else:
        newInstanceForm = UserCreationForm()
        # creating a new instance (then send it over to the template)
    
    context = {'form': newInstanceForm}
    
    return render(request, 'accounts/signup.html', context)

def login_view(request):
    if request.method =='POST':
        # pass the data here for validation, data is equals to request.POST, this is the syntax for this parameter
        postReqForm = AuthenticationForm(data=request.POST)
        if postReqForm.is_valid():
            # log in the user using .get_user()
            userFromLogin = postReqForm.get_user()
            # then use the login method and pass 2 parameters, the request and the user details
            login(request, userFromLogin)
            return redirect('store:mystore')
    else:
        authenticationForm = AuthenticationForm()
    
    context = {'form': authenticationForm}

    return render(request, 'accounts/login.html', context)