from django.db import models
from django.urls import reverse

# Create your models here.

class Passenger(models.Model):
    name = models.CharField(max_length=27)
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('passengers_detail', kwargs={'pk': self.id})


class Car(models.Model):
    year = models.IntegerField()
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    passengers = models.ManyToManyField(Passenger)
   
 
    def __str__(self):
        return f"The car {self.make} has id of {self.id}"
        
    def get_absolute_url(self):
        return reverse('detail', kwargs={'car_id': self.id})


TYPES = (
    ('O', 'Oil Change'),
    ('T', 'Tire Rotation'),
    ('C', 'Change Brake Fluid'),
)

class Service(models.Model):
    date = models.DateField('service date')
    type = models.CharField(
        max_length=1,
        choices=TYPES,
        blank=True
        )
    
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_type_display()} on {self.date}"

    class Meta:
        ordering = ['-date']