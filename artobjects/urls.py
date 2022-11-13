from django.urls import path

from . import views
from .views import ArtObjectsView, ArtObjectsDetailView, CreateArtObjectsView, ArtObjectsUpdateView, ObjectDeleteView

urlpatterns = [
    path('artobjects-list/', views.ArtObjectsView.as_view(), name='artobjects_list'),
    path('create-object/', views.CreateArtObjectsView.as_view(), name='create_object'),
    path('update-object/<int:pk>/', views.ArtObjectsUpdateView.as_view(), name='update_objects'),
    path('object-details/<int:pk>/', views.ArtObjectsDetailView.as_view(), name='object_details'),
    path('delete-object/<int:pk>/', views.ObjectDeleteView.as_view(), name='delete_object'),
]