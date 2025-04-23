# forms.py
from django import forms
from ..models import Car

class CarForm(forms.Form):
    brand = forms.CharField(max_length=100)
    model = forms.CharField(max_length=100)
    year = forms.IntegerField()
    price = forms.FloatField()
    description = forms.CharField(widget=forms.Textarea)
