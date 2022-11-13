from django.shortcuts import render, redirect
from django.urls import reverse_lazy

import artobjects
from .forms import ArtObjectsForm
from .models import ArtObjects
from django.views.generic import ListView, DetailView, CreateView, UpdateView


class ArtObjectsView(ListView):
    model = ArtObjects
    form_class = ArtObjectsForm
    context_object_name = 'artobjects_list'
    template_name = 'artobjects/artobjects_list.html'


class CreateArtObjectsView(CreateView):
    model = ArtObjects
    fields = '__all__'
    context_object_name = 'artobjects.product_name'
    template_name = 'artobjects/create_object.html'
    success_url = reverse_lazy('artobjects_list')

    def get_context_data(self, **kwargs):
        data = super(CreateArtObjectsView, self).get_context_data(**kwargs)
        artobjects = ArtObjects.objects.all()
        data['all_objects'] = artobjects

        return data


class ArtObjectsDetailView(DetailView):
    model = ArtObjects
    context_object_name = 'artobjects.description'
    template_name = 'artobjects/object_details.html'


class ArtObjectsUpdateView (UpdateView):
    template_name = 'artobjects/update_objects.html'
    model = ArtObjects
    form_class = ArtObjectsForm
    success_url = reverse_lazy('artobjects_list')
