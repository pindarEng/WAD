from django import forms
from .models import Product,User

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','price','category']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email']
        