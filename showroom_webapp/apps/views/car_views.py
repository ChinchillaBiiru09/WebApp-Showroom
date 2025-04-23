from django.shortcuts import render, redirect
from django.http import HttpResponse
from ..utilities.forms import CarForm
from ..utilities.db_helper import *
from ..utilities.queries import *
from ..utilities.utils import hpp_calculation, interest_rate_calculation, instalment_calculation



# CREATE DATA
# POST http://127.0.0.1:8000/car/create
def create_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            query = CAR_ADD_QUERY
            values = (data['brand'], data['model'], data['year'], data['price'], data['description'])
            car_id = save_data(query, values)

            # Get value of loan and interest rate from the form
            loan_amount = data.get('loan_amount')
            interest_rate = data.get('interest_rate')
            if loan_amount or interest_rate:
                query = LOAN_ADD_QUERY
                values = (car_id, data['loan'], data['interest_rate'])
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


# DELETE DATA
# POST http://127.0.0.1:8000/car/delete/(id)
def delete_car(request, id):
    print(request.method)
    if request.method == 'POST':
        query = CAR_DELETE_QUERY
        values = (id,)
        save_data(query, values)
        return redirect('index')
    else:
        return redirect('detail_car', id)


# DETAIL DATA
# GET http://127.0.0.1:8000/car/update/(id)
def detail_car(request, id):
    query = CAR_GET_BY_ID_QUERY
    values = (id,)
    car = get_data_with_values(query, values)

    query = SERVICE_GET_BY_CAR_QUERY
    services = get_data_with_values(query, values)

    query = LOAN_GET_BY_CAR_QUERY
    loans = get_data_with_values(query, values)
    interest_rate = 0
    instalment = 0
    if loans:
        interest_rate = interest_rate_calculation(loans[0]['loan'], loans[0]['interest_rate'], loans[0]['years'])
        instalment = instalment_calculation(loans[0]['loan'], loans[0]['interest_rate'], loans[0]['years'])
    hpp = hpp_calculation(car[0]['price'], services[0]['price']) if services else 0

    response = {
        'car': car[0], 
        'loans': loans, 
        'services': services,
        'hpp': hpp,
        'loans': loans,
        'interest_rate': interest_rate,
        'instalment': instalment,
        }

    if request.method == 'GET':
        return render(request, 'car/detail_car_page.html', response)
    else:
        return render(request, 'index')
