from django.urls import path

from . import views
from .views import ClothesView, CreateClothesView, ClothesUpdateView, ClothesDetailView, ClothesDeleteView

urlpatterns = [
    path('clotes-list/', views.ClothesView.as_view(), name='clothes_list'),
    path('create-clothes/', views.CreateClothesView.as_view(), name='create_clothes'),
    path('update-clothes/<int:pk>/', views.ClothesUpdateView.as_view(), name='update_clothes'),
    path('clothes-details/<int:pk>/', views.ClothesDetailView.as_view(), name='clothes_details'),
    path('delete-clothes/<int:pk>/', views.ClothesDeleteView.as_view(), name='delete_clothes'),
]