"""ScarletAuction URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views
from django.urls import path, include
from userextend.forms import AuthenticationNewForm, PasswordResetNewForm, SetPasswordNewForm
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('', include('userextend.urls')),
    path("login/", views.LoginView.as_view(form_class=AuthenticationNewForm), name="login"),
    path('', include('django.contrib.auth.urls')),
    path('artobjects/', include('artobjects.urls')),
    path('', include('clothes.urls')),
    path('', include('jewellery.urls')),
    path('', include('cars.urls')),
    path("password_reset/", views.PasswordResetView.as_view(form_class=PasswordResetNewForm), name="password_reset"),
    path('orders/', include('shopping_cart.urls')),
]