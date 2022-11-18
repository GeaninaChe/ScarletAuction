from django.urls import path
from .views import ShoppingCartPageView

urlpatterns = [
    path('', ShoppingCartPageView.as_view(), name='orders'),
]
