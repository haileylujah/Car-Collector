from django.shortcuts import render, redirect

#import the CreateView class
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

# Create your views here.
from django.http import HttpResponse
from .models import Car, Passenger
from .forms import ServiceForm


class CarCreate(CreateView):
  model = Car
  fields = '__all__'


class CarUpdate(UpdateView):
  model = Car
  fields = '__all__'

class CarDelete(DeleteView):
  model = Car
  success_url = '/cars/'


# Define the home view
def home(request):
  return render(request, 'about.html')

def about(request):
  return render(request, 'about.html')

# Add new view
def cars_index(request):
  cars = Car.objects.all()
  return render(request, 'cars/index.html', { 'cars': cars })

def cars_detail(request, car_id):
  car = Car.objects.get(id=car_id)
  # passengers_car_doesnt_has = Passenger.objects.exclude(id__in = car.passengers.all().values_list('id'))
  service_form = ServiceForm()

  return render(request, 'cars/detail.html', {
    'car': car, 
    'service_form': service_form,
    # 'passengers': passengers_car_doesnt_has
    })

def add_service(request, car_id):
  form = ServiceForm(request.POST)
  if form.is_valid():
    new_service = form.save(commit=False)
    new_service.car_id = car_id
    new_service.save()

  return redirect('detail', car_id=car_id)


def assoc_passenger(request, car_id, passenger_id):
  Car.objects.get(id=car_id).passengers.add(passenger_id)
  return redirect('detail', car_id=car_id)


class PassengerList(ListView):
  model = Passenger

class PassengerDetail(DetailView):
  model = Passenger

class PassengerCreate(CreateView):
  model = Passenger
  fields = '__all__'

class PassengerUpdate(UpdateView):
  model = Passenger
  fields = ['name', 'gender']

class PassengerDelete(DeleteView):
  model = Passenger
  success_url = '/passengers/'