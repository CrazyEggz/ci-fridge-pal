from django.urls import path
from . import views

# For test 
urlpatterns = [
    path('', views.Home.as_view(), name = 'home'),
    path('signup/', views.SignUp.as_view(), name = 'signup'),
]