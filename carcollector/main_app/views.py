from django.shortcuts import render, redirect

#import the CreateView class
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
from django.http import HttpResponse
from .models import Car
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
  return HttpResponse('<h1>Hello waaaaaaa /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
  return render(request, 'about.html')

# Add new view
def cars_index(request):
  cars = Car.objects.all()
  return render(request, 'cars/index.html', { 'cars': cars })

def cars_detail(request, car_id):
  car = Car.objects.get(id=car_id)
  service_form = ServiceForm()

  return render(request, 'cars/detail.html', {'car': car, 'service_form': service_form})

def add_service(request, car_id):
  form = ServiceForm(request.POST)
  if form.is_valid():
    new_service = form.save(commit=False)
    new_service.car_id = car_id
    new_service.save()

  return redirect('detail', car_id=car_id)