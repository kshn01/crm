import django
from django.forms import ModelForm
from .models import Order

from django.contrib.auth.forms import UserCreationForm
from django import  forms
from django.contrib.auth.models import User








class OrderForm(ModelForm):
    class Meta:
        model = Order  #whcih model to be used 
        fields = '__all__'

# -- User creation form 
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email' , 'password1', 'password2']

# ---