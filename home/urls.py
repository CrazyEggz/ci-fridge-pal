from . import views
from django.urls import path

# For test 
urlpatterns = [
    path('', views.Home.as_view(), name = 'home'),
]