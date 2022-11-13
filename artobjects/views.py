from django.shortcuts import render, redirect
from django.urls import reverse_lazy

import artobjects
from .forms import ArtObjectsForm
from .models import ArtObjects
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


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


class ArtObjectsDetailView(DetailView):
    model = ArtObjects
    context_object_name = 'artobjects.description'
    template_name = 'artobjects/object_details.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        all_details_artobjects = ArtObjects.objects.filter(artobjects_id=self.kwargs['pk'])
        data['all_details_artobjects'] = all_details_artobjects

        return data


class ArtObjectsUpdateView(UpdateView):
    template_name = 'artobjects/update_objects.html'
    model = ArtObjects
    form_class = ArtObjectsForm
    success_url = reverse_lazy('artobjects_list')


class ObjectDeleteView(DeleteView):
    template_name = 'artobjects/delete_object.html'
    model = ArtObjects
    success_url = reverse_lazy('artobjects_list')

