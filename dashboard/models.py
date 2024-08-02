from django.db import models
from django.contrib.auth.models import User

EXPIRY_DATE_TYPE = ((0, 'Best-before-date'), (1, 'Use-by-date'))

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.CharField(max_length=200)
    unit = models.ForeignKey('unit', on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)
    expiry_date = models.DateTimeField(null=True, blank=True)
    expiry_date_type = models.IntegerField(choices=EXPIRY_DATE_TYPE, null=True, blank=True)
    location = models.ForeignKey('Location', on_delete=models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=200)
    compartment = models.IntegerField()

    def __str__(self):
        return str(self.compartment)


class Unit(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
