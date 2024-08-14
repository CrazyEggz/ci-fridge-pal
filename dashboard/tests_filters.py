from datetime import date, timedelta
from django.contrib.auth.models import User
from django.test import TestCase

from .filters import ItemFilter
from .models import Item


class ItemFilterTestCase(TestCase):
    def setUp(self):
        user = User.objects.create()
        Item.objects.create(
            name='Garden Peas',
            quantity=5,
            expiry_date=date.today() + timedelta(days=7),
            location=0,
            user=user)
        Item.objects.create(
            name='Nearly Expired Garden Peas',
            quantity=5,
            expiry_date=date.today() + timedelta(days=1),
            location=1,
            user=user)
        Item.objects.create(
            name='Expired Garden Peas',
            quantity=5,
            expiry_date=date.today() - timedelta(days=1),
            location=1,
            user=user)

    def test_no_filter(self):
        items = Item.objects.all()
        items_filter = ItemFilter(data={}, queryset=items)
        result = items_filter.qs

        self.assertEqual(len(result), 3)

    def test_filter_location(self):
        items = Item.objects.all()
        items_filter = ItemFilter(data={'location': 1}, queryset=items)
        result = items_filter.qs

        self.assertEqual(len(result), 2)

    def test_filter_name_icontains(self):
        items = Item.objects.all()
        items_filter = ItemFilter(
            data={'name__icontains': 'peas'}, queryset=items)
        result = items_filter.qs

        self.assertEqual(len(result), 3)

    def test_filter_expiry_within_3days(self):
        items = Item.objects.all()
        items_filter = ItemFilter(data={'expiry_date': '3day'}, queryset=items)
        result = items_filter.qs

        self.assertEqual(len(result), 2)
