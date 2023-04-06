from django.db import models
from django.contrib.auth.models import User
from django_google_maps import fields as map_fields


class TaxiBooking(models.Model):
    phone = models.CharField(max_length=20)
    pickup = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    time = models.TimeField()
    message = models.TextField()

    def __str__(self):
        return self.name
    
class Booking(models.Model):
    location = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    vehicle_type = models.CharField(max_length=10)
    

# review
class review(models.Model):
    user= models.ForeignKey(User, models.CASCADE)
    comment = models.TextField(max_length=250)
    rate = models.IntegerField(default= 0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
    

