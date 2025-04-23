from django.shortcuts import render
from django.http import HttpResponse
from django.core.serializers import serialize
from ..utilities.forms import CarForm
from ..utilities.db_helper import *
from ..utilities.queries import CAR_ADD_QUERY, CAR_GET_ALL_QUERY, CAR_GET_BY_ID_QUERY
from ..models.car_models import Car

import json


# CREATE DATA
# POST http://127.0.0.1:8000/car/create
def create_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CarForm()

    return render(request, 'create_car_page.html', {'form': form})
    

# VIEW DATA
def view_car():
    cars = get_data(CAR_GET_ALL_QUERY)
    return cars


# UPDATE DATA
# PUT http://127.0.0.1:8000/car/update/(id)
def update_car(request, id):
    query = CAR_GET_BY_ID_QUERY
    values = (id)
    car = get_data_with_values(query, values)
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CarForm()
    return render(request, 'update_car_page.html', {'form': form, 'car': car})