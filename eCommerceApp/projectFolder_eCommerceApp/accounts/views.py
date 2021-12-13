from django.shortcuts import render, redirect
# also import redirect

# STEP 9 - USER CREATION FORM
from django.contrib.auth.forms import UserCreationForm

def signup(request):
    # if it's a post request
    if request.method =='POST':
        # passing all the values/data of the post request to a new instance
        form = UserCreationForm(request.POST)
        # if the form is valid (follows the instructions imbeded in django form) it saves the data
        # .is_valid() is a built in method that can check that, that returns boolean value
        if form.is_valid():
            form.save()
            # then redirect('appNameInUrl.py:urlName')
            return redirect('store:mystore')
    else:
        form = UserCreationForm()
        # creating a new instance (then send it over to the template)
    
    context = {'form': form}
    
    return render(request, 'accounts/signup.html', context)