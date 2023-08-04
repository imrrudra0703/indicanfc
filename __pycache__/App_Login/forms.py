from django.forms import ModelForm
from django import forms
from App_Login.models import *

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django_countries import countries
COUNTRY_CHOICES = tuple(countries)

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True,help_text='Enter Your Email Address')
    first_name = forms.CharField(max_length=30, required=True,help_text='Enter Your First Name')
    last_name = forms.CharField(max_length=30, required=True,help_text='Enter Your Last Name')
    country = forms.ChoiceField(choices=COUNTRY_CHOICES, required=True,help_text='Choose Your Country')
    phone = forms.CharField(max_length=20, required=True, help_text='Phone number')

    class Meta:
        model = User
        fields = ('email','first_name','last_name','country','phone','username', 'password1', 'password2',)

class UserProfileChange(UserChangeForm):
    class Meta:
        model=User
        fields=('username', 'email', 'first_name', 'last_name', 'password')

class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(

            Submit('submit', 'Subscribe', css_class='buton sbutton')
        )
