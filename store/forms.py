from django import forms

from .models import Product, Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'address', 'city', 'Telephone',)
        widgets = {
            'first_name': forms.TextInput(attrs={'style': 'width: 300px; height: 25px; margin-left: 8px; margin-top: 20px;'}),
            'last_name': forms.TextInput(attrs={'style': 'width: 300px; height: 25px; margin-left: 10px;margin-top: 20px;'}),
            'address': forms.TextInput(attrs={'style': 'width: 300px; height: 25px; margin-left: 22px;margin-top: 20px;'}),
            'city': forms.TextInput(attrs={'style': 'width: 300px; height: 25px; margin-left: 55px;margin-top: 20px;'}),
            'Telephone': forms.TextInput(attrs={'style': 'width: 300px; height: 25px; margin-left: 10px;margin-top: 20px;'}),

        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('category', 'title', 'description', 'price', 'image',)
        widgets = {
            'category': forms.Select(attrs={
                'style': 'width: 300px; height: 25px; margin-left: 22px; margin-top: 5px;'
            }),
            'title': forms.TextInput(attrs={
                'style': 'width: 300px; height: 25px; margin-left: 57px; margin-top: 10px;'
            }),
            'description': forms.Textarea(attrs={
                'style': 'width: 300px; height: 150px; margin-left: 8px; margin-top: 10px;'
            }),
            'price': forms.TextInput(attrs={
                'style': 'width: 300px; height: 25px; margin-left: 53px; margin-top: 10px;'
            }),
            'image': forms.FileInput(attrs={
                'style': 'width: 500px; height: 25px; margin-left: 45px; margin-top: 10px;'
            })
        }