from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Car

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
  return render(request, 'about.html')

# Add new view
def cars_index(request):
  cars = Car.objects.all()
  return render(request, 'cars/index.html', { 'cars': cars })

def cars_detail(request, car_id):
  car = Car.objects.get(id=car_id)
  return render(request, 'cars/detail.html', { 'car': car })