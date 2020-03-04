from django import forms
from .models import Products


class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['name', 'info', 'price', 'category']

    def clean_price(self):
        price = self.cleaned_data['price']
        if int(price) < 0:
            raise forms.ValidationError("The price must be bigger 0")
        return price
