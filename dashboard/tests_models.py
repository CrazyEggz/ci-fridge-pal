from datetime import date, timedelta
from django.contrib.auth.models import User
from django.test import TestCase

from .models import Item, Category, Unit


class ItemTestCase(TestCase):
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
            location=0,
            user=user)
        Item.objects.create(
            name='Expired Garden Peas',
            quantity=5,
            expiry_date=date.today() - timedelta(days=1),
            location=0,
            user=user)

    def test_item_not_near_expiry(self):
        item = Item.objects.get(name="Garden Peas")
        self.assertFalse(item.is_expired)
        self.assertFalse(item.will_expire_soon)

    def test_item_is_expired(self):
        item = Item.objects.get(name="Expired Garden Peas")
        self.assertTrue(item.is_expired)
        self.assertFalse(item.will_expire_soon)

    def test_item_will_expire_soon(self):
        item = Item.objects.get(name="Nearly Expired Garden Peas")
        self.assertTrue(item.will_expire_soon)


class CategoryTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Beverages")

    def test_can_get_category(self):
        category = Category.objects.get(name="Beverages")
        self.assertEqual(self.category.name, category.name)
        self.assertEqual(self.category.pk, category.pk)


class UnitTestCase(TestCase):
    def setUp(self):
        self.unit = Unit.objects.create(name="Pint(s)")

    def test_can_get_unit(self):
        unit = Unit.objects.get(name="Pint(s)")
        self.assertEqual(self.unit.name, unit.name)
        self.assertEqual(self.unit.pk, unit.pk)
