from django.contrib import admin
from .models import Car, Service, Passenger

# Register your models here.
admin.site.register(Car)
admin.site.register(Service)
admin.site.register(Passenger)