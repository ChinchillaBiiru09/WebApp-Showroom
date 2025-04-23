from django.shortcuts import render
from django.http import HttpResponse

from .car_views import view_car


def index(request):
    cars = view_car()
    return render(request, 'index.html', {'cars': cars})
