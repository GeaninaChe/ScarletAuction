from django.urls import path, include
from .views import ArtObjectsView, ArtObjectsDetailView

urlpatterns = [
    path('', ArtObjectsView.as_view(), name='artobjects_list'),
    path('<int:pk>', ArtObjectsView.as_view(), name='object_details'),
    path('', ArtObjectsView.as_view(), name='create_object'),
    path('', ArtObjectsDetailView.as_view(), name='update_objects'),
]
