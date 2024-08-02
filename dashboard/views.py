from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView, View
from .models import Item

# Create your views here.
class Dashboard(View):
    def get(self, request):
        items = Item.objects.filter(user=self.request.user.id).order_by('name')
        return render(request, 'dashboard/dashboard.html', {'items': items})
