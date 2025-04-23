from django.urls import path

from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("car/create", create_car, name="create_car"),
    path("car/edit/<id>", update_car, name="update_car"),
    path("car/delete/<id>", delete_car, name="delete_car"),
    path("car/detail/<id>", detail_car, name="detail_car"),
]