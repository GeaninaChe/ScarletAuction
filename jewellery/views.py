from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import JewelleryForm
from .models import Jewellery
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class JewelleryView(ListView):
    template_name = 'jewellery/jewellery_list.html'
    model = Jewellery
    form_class = JewelleryForm
    context_object_name = 'jewellery_list'


class CreateJewelleryView(CreateView):
    template_name = 'jewellery/create_jewellery.html'
    model = Jewellery
    fields = '__all__'
    context_object_name = 'jewellery.product_name'
    success_url = reverse_lazy('jewellery_list')


class JewelleryDetailView(DetailView):
    template_name = 'jewellery/jewellery_details.html'
    model = Jewellery
    context_object_name = 'jewellery.description'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        all_details_jewellery = Jewellery.objects.filter(product_name=self.kwargs['pk'])
        data['all_details_jewellery'] = all_details_jewellery

        return data


class JewelleryUpdateView(UpdateView):
    template_name = 'jewellery/update_jewellery.html'
    model = Jewellery
    form_class = JewelleryForm
    success_url = reverse_lazy('jewellery_list')


class JewelleryDeleteView(DeleteView):
    template_name = 'jewellery/delete_jewellery.html'
    model = Jewellery
    success_url = reverse_lazy('jewellery_list')