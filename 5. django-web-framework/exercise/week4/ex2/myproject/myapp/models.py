from django.db import models

# Create your models here.
class Reservation(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    booking_time = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.first_name