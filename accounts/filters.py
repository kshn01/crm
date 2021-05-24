# similar to modelforms (forms.py)
#create filter form based upon the model

from django.db.models import fields
import django_filters
from django_filters.filterset import filterset_factory
from .models import *

from django_filters import DateFilter






class OrderFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="date_created", lookup_expr="gte")
    end_date = DateFilter(field_name="date_created", lookup_expr="lte")
    class Meta:
        model = Order
        fields = '__all__' 
        exclude = ['customer', 'date_created']
