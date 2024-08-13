from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


# For test 
urlpatterns = [
    path('', views.Home.as_view(), name = 'home'),
    path('register/', views.Register.as_view(), name = 'register'),
    path('login/', auth_views.LoginView.as_view(template_name = 'home/login.html', redirect_authenticated_user = True), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'home/logout.html'), name = 'logout'),
]
