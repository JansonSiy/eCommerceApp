# STEP 12 - UPDATE USER MODEL & FORM
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms

class RegisterUserForm(UserCreationForm):
    # INITIAL
    # first_name = forms.CharField(max_length=50, required=False)
    # last_name = forms.CharField(max_length=50, required=False)
    # email = forms.EmailField(required=False)

    # FINAL
    # reference: https://medium.com/swlh/how-to-style-your-django-forms-7e8463aae4fa
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'username', 'style': 'width: 50%;', 'class': 'form-control form-control-sm marginBottom'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'password', 'style': 'width: 50%;', 'class': 'form-control form-control-sm marginBottom'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'reconfirm password', 'style': 'width: 50%;', 'class': 'form-control form-control-sm marginBottom'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'first name', 'style': 'width: 50%;', 'class': 'form-control form-control-sm marginBottom'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'last name', 'style': 'width: 50%;', 'class': 'form-control form-control-sm marginBottom'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'email', 'style': 'width: 50%; margin-bottom: 20px;', 'class': 'form-control form-control-sm'}))

    # reference https://stackoverflow.com/questions/21572701/customize-the-way-usercreationform-looks-in-django
    # how to properly add a class to an inbuilt form
    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)

        # INITIAL
        # self.fields['username'].widget.attrs['class'] = 'form-control form-control-sm'
        # self.fields['password1'].widget.attrs['class'] = 'form-control form-control-sm'
        # self.fields['password2'].widget.attrs['class'] = 'form-control form-control-sm'
        # self.fields['first_name'].widget.attrs['class'] = 'form-control form-control-sm'
        # self.fields['last_name'].widget.attrs['class'] = 'form-control form-control-sm'
        # self.fields['email'].widget.attrs['class'] = 'form-control form-control-sm'
        
        # reference: https://stackoverflow.com/questions/13202845/removing-help-text-from-django-usercreateform
        # removes all help_text
        for removeAllHelpText in ['username', 'password1', 'password2']:
            self.fields[removeAllHelpText].help_text = None

        # reference: https://stackoverflow.com/questions/22363157/changing-the-required-field-text-on-a-modelform-in-django
        # this changes the default error_message
        # reference:  https://stackoverflow.com/questions/18995225/django-how-to-remove-bullet-point-when-printing-form-errors
        # this removes the • in the error message (please check css file)
        self.fields['username'].error_messages = {'required': '*this field is required to be unique'}

        # reference: https://stackoverflow.com/questions/13202845/removing-help-text-from-django-usercreateform
        # removes '• This field is required'
        for removeRequiredErrorMessage in ['password1', 'password2', 'first_name', 'last_name', 'email']:
            self.fields[removeRequiredErrorMessage].required = False

        # reference: https://stackoverflow.com/questions/11947001/change-the-name-attribute-of-form-field-in-django-template-using
        # renames the default labels
        self.fields['password1'].label = "Password"
        self.fields['password2'].label = "Reconfirm Password"
        self.fields['first_name'].label = "First Name"
        self.fields['last_name'].label = "Last Name"
        self.fields['email'].label = "Email Address"

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'email')

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'username', 'style': 'width: 50%;', 'class': 'form-control form-control-sm marginBottom'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'password', 'style': 'width: 50%; margin-bottom: 20px;', 'class': 'form-control form-control-sm marginBottom'}))

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        self.fields['username'].error_messages = {'required': '*these fields are required'}

        self.fields['password'].required = False

        self.fields['username'].label = "Username"
        self.fields['password'].label = "Password"