from django.urls import path

from . import views
from .views import ArtObjectsView, ArtObjectsDetailView, CreateArtObjectsView, ArtObjectsUpdateView

urlpatterns = [
    # path('', ArtObjectsView.as_view(), name='artobjects_list'),
    path('artobjects-list/', views.ArtObjectsView.as_view(), name='artobjects_list'),
    path('<int:pk>', ArtObjectsView.as_view(), name='artobjects_detail'),
    path('', CreateArtObjectsView.as_view(), name='create_object'),
    path('', ArtObjectsUpdateView.as_view(), name='update_objects')
]
