from django.db import models

# Create your models here.
class Person(models.Model): 
    name = models.CharField(max_length=50) 
    address = models.CharField(max_length=80, default='Addis Ababa')
    email = models.EmailField()



class Logger(models.Model):
    first_name = models.CharField(max_length=50) 
    last_name = models.CharField(max_length=50) 
    time_log = models.TimeField(help_text= "Enter the exact time")
    
    
class Reservation(models.Model):
    name = models.CharField(max_length=100, blank=True)
    contact = models.CharField('Phone Number', max_length=300)
    time = models.TimeField()
    count = models.IntegerField()
    notes = models.CharField(max_length=300, blank=True)
    
    # print user names in admin db
    def __str__(self):
        return self.name
    

class Product(models.Model): 
    ProductID: models.IntegerField() 
    name : models.TextField() 
    category : models.TextField 
    class Meta: 
        permissions = [('can_change_category', 'Can change category')] 