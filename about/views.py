from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import TemplateView # For test

# Create your views here.

# For test
class About(TemplateView):
    template_name = 'base.html'