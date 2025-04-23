from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.serializers import serialize
from ..utilities.forms import CarForm
from ..utilities.db_helper import *
from ..utilities.queries import CAR_ADD_QUERY, CAR_GET_ALL_QUERY, CAR_GET_BY_ID_QUERY, CAR_DELETE_QUERY, CAR_UPDATE_QUERY
# from .home_views import index


# CREATE DATA
# POST http://127.0.0.1:8000/car/create
def create_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            query = CAR_ADD_QUERY
            values = (data['brand'], data['model'], data['year'], data['price'], data['description'])
            save_data(query, values)
            return redirect('index')
        else:
            return HttpResponse("Invalid form data")
    else:
        form = CarForm()

    return render(request, 'car/create_car_page.html', {'form': form})
    

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
    print(car)
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CarForm()
    return render(request, 'create_car_page.html', {'form': form, 'car': car})


# DELETE DATA
# DEL http://127.0.0.1:8000/car/delete/(id)
def delete_car(request, id):
    print(request.method)
    if request.method == 'POST':
        query = CAR_DELETE_QUERY
        values = (id,)
        print(values)
        dell = save_data(query, values)
        print(dell)
        return redirect('index')
    else:
        return redirect(detail_car, id)


# DETAIL DATA
# GET http://127.0.0.1:8000/car/update/(id)
def detail_car(request, id):
    query = CAR_GET_BY_ID_QUERY
    values = (id,)
    car = get_data_with_values(query, values)
    if request.method == 'GET':
        return render(request, 'car/detail_car_page.html', {'car': car})
    else:
        return render(request, 'create_car_page.html', {'car': car})
