from django.urls import path

from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("car/create", create_car, name="create_car"),
    path("car/edit", update_car, name="update_car"),
]