from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView, View
from .models import Item

# Create your views here.
class Dashboard(View):
    def get(self, request):
        return render(request, 'dashboard/dashboard.html')
