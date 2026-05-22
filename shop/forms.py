from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'quantity_ml', 'details', 'image', 'dealer_handle']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full p-3 border rounded-lg mb-4'}),
            'price': forms.NumberInput(attrs={'class': 'w-full p-3 border rounded-lg mb-4'}),
            'quantity_ml': forms.NumberInput(attrs={'class': 'w-full p-3 border rounded-lg mb-4'}),
            'details': forms.Textarea(attrs={'class': 'w-full p-3 border rounded-lg mb-4', 'rows': 4}),
            'dealer_handle': forms.TextInput(attrs={'class': 'w-full p-3 border rounded-lg mb-4', 'placeholder': 'e.g. 2348000000000'}),
            'image': forms.FileInput(attrs={'class': 'mb-4'}),
        }