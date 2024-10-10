from django import forms
from . models import Category, product

class Categoryform(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class Productform(forms.ModelForm):
    class Meta:
        model = product
        fields =['category','name','rate','images','description']  