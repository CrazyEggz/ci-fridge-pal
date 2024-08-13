from django.db import models
from django.contrib.auth.models import User


EXPIRY_DATE_TYPE = ((0, 'Best-before-date'), (1, 'Use-by-date'))
AREA = ((0, 'Fridge'), (1, 'Freezer'))


class Item(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.IntegerField()
    unit = models.ForeignKey(
        'unit', on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(
        'Category', on_delete=models.SET_NULL, null=True, blank=True)
    expiry_date = models.DateField(null=True, blank=True)
    expiry_date_type = models.IntegerField(
        choices=EXPIRY_DATE_TYPE, null=True, blank=True)
    location = models.IntegerField(choices=AREA)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Unit(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
