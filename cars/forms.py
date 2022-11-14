from django import forms
from django.forms import TextInput, Textarea, DateInput

from cars.models import Car


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        # fields = '__all__'
        fields = ['product_name', 'description', 'starting_price', 'final_price']

        widgets = {
            'product_name': TextInput(attrs={'placeholder': 'Please enter the car name:', 'class': 'form-control'}),
            'description': TextInput(attrs={'placeholder': 'Please enter the car description:', 'class': 'form-control'}),
            'starting_price': TextInput(attrs={'placeholder': 'Please enter the starting price:', 'class': 'form-control'}),
            'final_price': TextInput(attrs={'placeholder': 'Please enter the final price:', 'class': 'form-control'})
        }