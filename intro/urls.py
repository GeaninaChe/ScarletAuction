from django.urls import path
from intro import views


urlpatterns = [
    path('index/', views.index, name='index'),
]
