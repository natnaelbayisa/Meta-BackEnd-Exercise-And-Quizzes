from django.contrib import admin
from .models import Logger, Reservation

# Register your models here.
admin.site.register(Logger)

admin.site.register(Reservation)