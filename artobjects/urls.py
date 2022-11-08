from django.urls import path
from artobjects import views

urlpatterns = [
    path('artobjects_api/', views.ArtObjectsApi.as_view(), name='artobjects-api')
]