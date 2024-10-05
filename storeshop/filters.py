from django_filters import FilterSet
from .models import Product

class ProductFilter(FilterSet):
    class Meta:
        model = Product
        fields = {
            'price': ['gt', 'lt'],
            'date': ['gt', 'lt'],
            'active': ['exact'],
            'category': ['exact']
        }