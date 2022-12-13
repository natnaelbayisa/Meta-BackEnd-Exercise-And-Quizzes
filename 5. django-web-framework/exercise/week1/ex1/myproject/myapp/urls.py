from django.urls import path
from . import views

# http://127.0.0.1:8000/welcome/welcomeback

urlpatterns = [
    path('welcomeback', views.welcome, name="welcome"),  
    
]