from django.shortcuts import render, redirect
from django.urls import reverse_lazy

import artobjects
from .forms import CarForm
from .models import Car
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class CarView(ListView):
    template_name = 'cars/cars_list.html'
    model = Car
    form_class = CarForm
    context_object_name = 'cars_list'


class CreateCarView(CreateView):
    template_name = 'cars/create_car.html'
    model = Car
    fields = '__all__'
    context_object_name = 'car.product_name'
    success_url = reverse_lazy('cars_list')


class CarDetailView(DetailView):
    template_name = 'cars/car_details.html'
    model = Car
    context_object_name = 'car.description'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        all_details_cars = Car.objects.filter(product_name=self.kwargs['pk'])
        data['all_details_cars'] = all_details_cars

        return data


class CarUpdateView(UpdateView):
    template_name = 'cars/update_car.html'
    model = Car
    form_class = CarForm
    success_url = reverse_lazy('cars_list')


class CarDeleteView(DeleteView):
    template_name = 'cars/delete_car.html'
    model = Car
    success_url = reverse_lazy('cars_list')
