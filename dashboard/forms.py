from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    expiry_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    class Meta:
        model = Item
        fields = ['name', 'quantity', 'unit', 'category', 'expiry_date', 'expiry_date_type', 'location']