# forms.py
from django import forms
# from ..models import Car
from ..utilities.db_helper import get_data
from ..utilities.queries import CAR_GET_ALL_QUERY


class CarForm(forms.Form):
    brand = forms.CharField(max_length=100)
    model = forms.CharField(max_length=100)
    year = forms.IntegerField()
    price = forms.FloatField()
    description = forms.CharField(widget=forms.Textarea)

class ServiceForm(forms.Form):
    car = forms.ChoiceField(
        choices=[],
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    price = forms.FloatField()
    description = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Ambil data dari query manual
        cars = get_data(CAR_GET_ALL_QUERY)
        
        # Ubah jadi list tuple (id, nama)
        choices = [(car['id'], f"{car['brand']} {car['model']}") for car in cars]
        
        # Set choices ke field form
        self.fields['car'].choices = [('', '-- Pilih Mobil --')] + choices
