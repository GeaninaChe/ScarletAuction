from django.urls import path

from . import views
from .views import JewelleryView, CreateJewelleryView, JewelleryUpdateView, JewelleryDetailView, JewelleryDeleteView

urlpatterns = [
    path('jewellery-list/', views.JewelleryView.as_view(), name='jewellery_list'),
    path('create-jewellery/', views.CreateJewelleryView.as_view(), name='create_jewellery'),
    path('update-jewellery/<int:pk>/', views.JewelleryUpdateView.as_view(), name='update_jewellery'),
    path('jewellery-details/<int:pk>/', views.JewelleryDetailView.as_view(), name='jewellery_details'),
    path('delete-jewellery/<int:pk>/', views.JewelleryDeleteView.as_view(), name='delete_jewellery'),
]