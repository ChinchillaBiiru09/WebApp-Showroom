from django.shortcuts import render
from .car_views import view_car



# HOME PAGE
# GET http://127.0.0.1:8000/
def index(request):
    cars = view_car()
    return render(request, 'index.html', {'cars': cars})
