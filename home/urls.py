from django.urls import path

from home import views

urlpatterns = [
    path('', views.HomeTemplateView.as_view(), name="homepage"),
    path('', views.IntroductionView.as_view(), name="our_story"),
]