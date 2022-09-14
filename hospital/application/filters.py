from cgitb import lookup
import django_filters
from django_filters import CharFilter
from .models import *
class OrderFilter(django_filters.FilterSet):
    # start_date  = DateFilter(field_name='date_created',lookup_expr= 'gte')
    # end_date  = DateFilter(field_name='date_created',lookup_expr= 'lte')
    note = CharFilter(field_name='ID_number',lookup_expr= 'icontains')
    class Meta:
        model = Patient
        fields = '__all__'
        exclude = ['date_created']
