from datetime import date
from django.test import TestCase

from .models import Category
from .forms import ItemForm


class ItemFormTestCase(TestCase):
    minimum_form_data = {
        'name': 'Garden Peas',
        'quantity': 5,
        'expiry_date': date.today(),
        'location': '1',
    }

    def setUp(self):
        self.category = Category.objects.create(name="Vegetables")

    def test_required_fields(self):
        form = ItemForm(data={})

        self.assertFormError(form, 'name', errors='This field is required.')
        self.assertFormError(
            form, 'quantity', errors='This field is required.')
        self.assertFormError(
            form, 'expiry_date', errors='This field is required.')
        self.assertFormError(
            form, 'location', errors='This field is required.')
        self.assertFalse(form.is_valid())

    def test_minimum_required_fields(self):
        form = ItemForm(data=self.minimum_form_data)

        self.assertTrue(form.is_valid())

    def test_invalid_location(self):
        data = self.minimum_form_data.copy()
        data['location'] = 993399
        form = ItemForm(data=data)

        self.assertFormError(
            form,
            'location',
            errors='Select a valid choice.'
            + ' 993399 is not one of the available choices.')
        self.assertFalse(form.is_valid())

    def test_invalid_expiry_date_type(self):
        data = self.minimum_form_data.copy()
        data['expiry_date_type'] = 993399
        form = ItemForm(data=data)

        self.assertFormError(
            form,
            'expiry_date_type',
            errors='Select a valid choice.'
            + ' 993399 is not one of the available choices.')
        self.assertFalse(form.is_valid())

    def test_valid_category(self):
        data = self.minimum_form_data.copy()
        data['category'] = self.category.pk
        form = ItemForm(data=data)

        self.assertTrue(form.is_valid())

    def test_invalid_category(self):
        data = self.minimum_form_data.copy()
        data['category'] = 993399
        form = ItemForm(data=data)

        self.assertFormError(
            form,
            'category',
            errors='Select a valid choice.'
            + ' That choice is not one of the available choices.')
        self.assertFalse(form.is_valid())
