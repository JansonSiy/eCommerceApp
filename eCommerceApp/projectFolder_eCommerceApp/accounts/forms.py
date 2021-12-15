# STEP 12 - UPDATE USER MODEL & FORM
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegisterUserForm(UserCreationForm):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()
    # age = forms.IntegerField()
    # gender = forms.CharField(max_length=50)
    # address = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        # fields = ('username', 'first_name', 'last_name', 'email', 'age', 'gender', 'address', 'password1', 'password2')