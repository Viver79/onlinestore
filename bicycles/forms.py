from django import forms
from django.forms import ModelForm
from .models import Bike_type, Bike_brand, ProductBicycles

class Bike_typeForm(forms.ModelForm):
    title = forms.CharField(max_length=50,
                            widget=forms.TextInput(attrs={'placeholder': "Name", 'required': "required"}))
    categories_bicycles = forms.IntegerField(
        widget=forms.TextInput(attrs={'placeholder': "Type", 'required': "required"}))
    is_visible = forms.BooleanField(widget=forms.CheckboxInput(attrs={'required':'required'}))

    class Meta(object):
        model = Bike_type
        fields = ('title', 'categories_bicycles', 'is_visible')

class Bike_brandForm(forms.ModelForm):
    title = forms.CharField(max_length=50,
                            widget=forms.TextInput(attrs={'placeholder': "Name", 'required': "required"}))
    categories_bicycles = forms.IntegerField(
        widget=forms.TextInput(attrs={'placeholder': "Type", 'required': "required"}))
    is_visible = forms.BooleanField(widget=forms.CheckboxInput(attrs={'required':'required'}))

    class Meta(object):
        model = Bike_brand
        fields = ('title', 'categories_bicycles', 'is_visible')

