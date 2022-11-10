from django.shortcuts import render
from .models import ArtObjects
from django.views.generic import ListView, DetailView


class ArtObjectsView(ListView):
    model = ArtObjects
    context_object_name = 'artobjects_list'
    template_name = 'artobjects/create_object.html'


class ArtObjectsDetailView(DetailView):
    model = ArtObjects
    context_object_name = 'artobjects.product_name'
    template_name = 'artobjects/object_details.html'

