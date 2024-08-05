from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, View
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Item
from .forms import ItemForm

# Create your views here.
class Dashboard(View):
    def get(self, request):
        items = Item.objects.filter(user=self.request.user.id).order_by('name')
        return render(request, 'dashboard/dashboard.html', {'items': items})


class AddItem(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Item
    form_class = ItemForm
    template_name = 'dashboard/item_form.html'
    success_url = reverse_lazy('dashboard')
    success_message = "Item %(name)s was added successfully."

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditItem(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Item
    form_class = ItemForm
    template_name = 'dashboard/item_form.html'
    success_url = reverse_lazy('dashboard')
    success_message = "Item %(name)s was updated successfully."
