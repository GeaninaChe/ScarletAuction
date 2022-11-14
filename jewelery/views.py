from django.shortcuts import render, redirect
from django.urls import reverse_lazy

import artobjects
from .forms import JeweleryForm
from .models import Jewelery
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class JeweleryView(ListView):
    template_name = 'jewelery/jewelery_list.html'
    model = Jewelery
    form_class = JeweleryForm
    context_object_name = 'jewelery_list'


class CreateJeweleryView(CreateView):
    template_name = 'jewelery/create_jewelery.html'
    model = Jewelery
    fields = '__all__'
    context_object_name = 'jewelery.product_name'
    success_url = reverse_lazy('jewelery_list')


class JeweleryDetailView(DetailView):
    template_name = 'jewelery/jewelery_details.html'
    model = Jewelery
    context_object_name = 'jewelery.description'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        all_details_jewelery = Jewelery.objects.filter(product_name=self.kwargs['pk'])
        data['all_details_jewelery'] = all_details_jewelery

        return data


class JeweleryUpdateView(UpdateView):
    template_name = 'jewelery/update_clothes.html'
    model = Jewelery
    form_class = JeweleryForm
    success_url = reverse_lazy('jewelery_list')


class JeweleryDeleteView(DeleteView):
    template_name = 'jewelery/delete_jewelery.html'
    model = Jewelery
    success_url = reverse_lazy('jewelery_list')