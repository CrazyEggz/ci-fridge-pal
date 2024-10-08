from django.urls import path
from . import views


urlpatterns = [
    path('dashboard/', views.Dashboard.as_view(), name='dashboard'),
    path('dashboard/add-item', views.AddItem.as_view(), name='add-item'),
    path(
        'dashboard/edit-item/<int:pk>',
        views.EditItem.as_view(),
        name='edit-item'),
    path(
        'dashboard/delete-item/<int:pk>',
        views.DeleteItem.as_view(),
        name='delete-item')
]
