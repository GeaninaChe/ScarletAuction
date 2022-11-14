from django.urls import path

from . import views
from .views import JeweleryView, CreateJeweleryView, JeweleryUpdateView, JeweleryDetailView, JeweleryDeleteView

urlpatterns = [
    path('jewelery-list/', views.JeweleryView.as_view(), name='jewelery_list'),
    path('create-jewelery/', views.CreateJeweleryView.as_view(), name='create_jewelery'),
    path('update-jewelery/<int:pk>/', views.JeweleryUpdateView.as_view(), name='update_jewelery'),
    path('jewelery-details/<int:pk>/', views.JeweleryDetailView.as_view(), name='jewelery_details'),
    path('delete-jewelery/<int:pk>/', views.JeweleryDeleteView.as_view(), name='delete_jewelery'),
]