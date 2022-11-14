from django.urls import path

from . import views
from .views import CarView, CreateCarView, CarUpdateView, CarDetailView, CarDeleteView

urlpatterns = [
    path('cars-list/', views.CarView.as_view(), name='cars_list'),
    path('create-car/', views.CreateCarView.as_view(), name='create_car'),
    path('update-car/<int:pk>/', views.CarUpdateView.as_view(), name='update_car'),
    path('car-details/<int:pk>/', views.CarDetailView.as_view(), name='car_details'),
    path('delete-car/<int:pk>/', views.CarDeleteView.as_view(), name='delete_car'),
]