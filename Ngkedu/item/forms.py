from django import forms
from .models import Item

INPUT_CLASSES = 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent'

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['category', 'name', 'description', 'price', 'image']
        widgets = {
            'category': forms.Select(attrs={'class': INPUT_CLASSES}),
            'name': forms.TextInput(attrs={'class': INPUT_CLASSES, 'placeholder': 'Item Name'}),
            'description': forms.Textarea(attrs={'class': INPUT_CLASSES, 'placeholder': 'Item Description', 'rows': 4}),
            'price': forms.NumberInput(attrs={'class': INPUT_CLASSES, 'placeholder': 'Item Price'}),
            'image': forms.ClearableFileInput(attrs={'class': INPUT_CLASSES}),
        }

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description', 'price', 'image', 'is_sold']
        widgets = {
            'name': forms.TextInput(attrs={'class': INPUT_CLASSES, 'placeholder': 'Item Name'}),
            'description': forms.Textarea(attrs={'class': INPUT_CLASSES, 'placeholder': 'Item Description', 'rows': 4}),
            'price': forms.NumberInput(attrs={'class': INPUT_CLASSES, 'placeholder': 'Item Price'}),
            'image': forms.ClearableFileInput(attrs={'class': INPUT_CLASSES}),
        }