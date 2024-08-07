import django_filters

from .models import Item

class ItemFilter(django_filters.FilterSet):
    expiry_date = django_filters.DateFromToRangeFilter()

    class Meta:
        model = Item
        fields = {
            'name': ['icontains'],
            'category': ['exact'],
            'location': ['exact'],
            'expiry_date': ['exact'],
        }
