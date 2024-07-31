from . import views
from django.urls import path

# For test 
urlpatterns = [
    path('', views.About.as_view(), name = 'homepage'),
]