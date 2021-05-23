from django.forms import ModelForm
from .models import Order









class OrderForm(ModelForm):
    class Meta:
        model = Order  #whcih model to be used 
        fields = '__all__'