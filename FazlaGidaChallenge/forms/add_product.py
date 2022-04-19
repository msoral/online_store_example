from django import forms

from ..models import Product


class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "slug", "description", "price", "category"]
