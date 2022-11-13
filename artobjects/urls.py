from django.urls import path

from . import views
from .views import ArtObjectsView, ArtObjectsDetailView, CreateArtObjectsView, ArtObjectsUpdateView, ObjectDeleteView

urlpatterns = [
    path('artobjects-list/', views.ArtObjectsView.as_view(), name='artobjects_list'),
    path('', CreateArtObjectsView.as_view(), name='create_object'),
    path('', ArtObjectsUpdateView.as_view(), name='update_objects'),
    path('', ArtObjectsDetailView.as_view(), name='object_details'),
    path('', views.ObjectDeleteView.as_view(), name='delete_object'),
]
