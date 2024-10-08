from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Item
from .forms import ItemForm
from .filters import ItemFilter


class Dashboard(LoginRequiredMixin, View):
    def get(self, request):
        user_id = self.request.user.id
        items = Item.objects.filter(user=user_id).order_by('expiry_date')
        items_filter = ItemFilter(request.GET, queryset=items)
        items_filter_applied = Dashboard.isItemFilterApplied(items_filter)

        expired_count = 0
        expiring_soon_count = 0
        for item in items_filter.qs:
            if item.is_expired:
                expired_count += 1
            elif item.will_expire_soon:
                expiring_soon_count += 1

        return render(request, 'dashboard/dashboard.html', {
            'location': request.GET.get('location', default=''),
            'items': items_filter.qs,
            'items_filter': items_filter,
            'items_filter_applied': items_filter_applied,
            'expired_count': expired_count,
            'expiring_soon_count': expiring_soon_count,
        })

    def isItemFilterApplied(items_filter):
        if not items_filter.form.is_valid():
            return False

        for key, value in items_filter.form.cleaned_data.items():
            if key != "location" and value != '' and value is not None:
                return True

        return False


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


class DeleteItem(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Item
    success_url = reverse_lazy('dashboard')
    success_message = "Item was deleted successfully."
