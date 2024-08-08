import django_filters
import datetime
from django import forms

from .models import Item

EXPIRY_DATE_CHOICES = (('', '---------'), ('0day', 'Today'), ('1day', '1 Day'), ('3day', '3 Days'), ('7day', '7 Days'))

def expiryDateChoiceToDate(choice):
    """
    Convert the user's expiry date choices to an actual date
    """
    current_date = datetime.date.today()
    match choice:
        case '0day': return current_date
        case '1day': return current_date + datetime.timedelta(days=1)
        case '3day': return current_date + datetime.timedelta(days=3)
        case '7day': return current_date + datetime.timedelta(days=7)


class ItemFilter(django_filters.FilterSet):
    expiry_date = django_filters.TypedChoiceFilter(choices = EXPIRY_DATE_CHOICES, label='Expires within', lookup_expr='lt', coerce=expiryDateChoiceToDate)
    location = django_filters.NumberFilter(widget = forms.HiddenInput())

    class Meta:
        model = Item
        fields = {
            'name': ['icontains'],
            'category': ['exact'],
        }
