from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.serializers import serialize
from ..utilities.forms import ServiceForm
from ..utilities.db_helper import *
from ..utilities.queries import SERVICE_ADD_QUERY


# CREATE DATA
# POST http://127.0.0.1:8000/service/create
def create_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            query = SERVICE_ADD_QUERY
            values = (data['car'], data['price'], data['description'])
            save_data(query, values)
            return redirect('index')
        else:
            return HttpResponse("Invalid form data")
    else:
        form = ServiceForm()
    return render(request, 'service/create_service_page.html', {'form': form})
    