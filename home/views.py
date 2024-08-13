from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView, View
from django.contrib.auth import authenticate, login
from .forms import RegisterForm

# Create your views here.

class Register(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'home/register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password1']
            )
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'home/register.html', {'form': form})

# For test
class Home(TemplateView):
    template_name = 'home/home.html'