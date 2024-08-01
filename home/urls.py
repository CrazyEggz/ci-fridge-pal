from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


# For test 
urlpatterns = [
    path('', views.Home.as_view(), name = 'home'),
    path('signup/', views.SignUp.as_view(), name = 'signup'),
    path('login/', auth_views.LoginView.as_view(template_name = 'home/login.html'), name = 'login'),
]
