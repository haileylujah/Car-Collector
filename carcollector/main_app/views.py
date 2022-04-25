from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
  return render(request, 'about.html')

# Add new view
def cars_index(request):
  return render(request, 'cars/index.html', { 'cars': cars })

class car:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

cars = [
  car('Lolo', 'tabby', 'foul little demon', 3),
  car('Sachi', 'tortoise shell', 'diluted tortoise shell', 0),
  car('Raven', 'black tripod', '3 legged car', 4)
]