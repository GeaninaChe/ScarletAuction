from django import forms
from django.forms import TextInput, Textarea, DateInput

from artobjects.models import ArtObjects


class ArtObjectsForm(forms.ModelForm):
    class Meta:
        model = ArtObjects
        # fields = '__all__'
        fields = ['product_name', 'description', 'starting_price', 'final_price']

        widgets = {
            'product_name': TextInput(attrs={'placeholder': 'Please enter the product name:', 'class': 'form-control'}),
            'description': TextInput(attrs={'placeholder': 'Please enter the product description:', 'class': 'form-control'}),
            'starting_price': TextInput(attrs={'placeholder': 'Please enter the starting price:', 'class': 'form-control'}),
            'final_price': TextInput(attrs={'placeholder': 'Please enter the final price:', 'class': 'form-control'})
        }