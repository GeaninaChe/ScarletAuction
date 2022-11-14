from django.shortcuts import render, redirect
from django.urls import reverse_lazy


from .forms import ClothesForm
from .models import Clothes
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class ClothesView(ListView):
    template_name = 'clothes/clothes_list.html'
    model = Clothes
    form_class = ClothesForm
    context_object_name = 'clothes_list'


class CreateClothesView(CreateView):
    template_name = 'clothes/create_clothes.html'
    model = Clothes
    fields = '__all__'
    context_object_name = 'clothes.product_name'
    success_url = reverse_lazy('clothes_list')


class ClothesDetailView(DetailView):
    template_name = 'clothes/clothes_details.html'
    model = Clothes
    context_object_name = 'clothes.description'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        all_details_clothes = Clothes.objects.filter(product_name=self.kwargs['pk'])
        data['all_details_clothes'] = all_details_clothes

        return data


class ClothesUpdateView(UpdateView):
    template_name = 'clothes/update_clothes.html'
    model = Clothes
    form_class = ClothesForm
    success_url = reverse_lazy('clothes_list')


class ClothesDeleteView(DeleteView):
    template_name = 'clothes/delete_clothes.html'
    model = Clothes
    success_url = reverse_lazy('clothes_list')


