from django.urls import path
from .views import ArtObjectsView, ArtObjectsDetailView

urlpatterns = [
    path('', ArtObjectsView.as_view(), name='artobjects'),
    path('<int:pk>', ArtObjectsView.as_view(), name='artobjects_detail'),
    path('', ArtObjectsView.as_view(), name='create_object'),
    path('', ArtObjectsDetailView.as_view(), name='object_details')
]
