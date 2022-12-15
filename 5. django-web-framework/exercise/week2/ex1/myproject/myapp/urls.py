from django.urls import path

from . import views

urlpatterns = [
    path("dishes/<str:dish>", views.foodItems, name="dish_name"),
    
    # http://127.0.0.1:8000/tea
    # path("<str:drink_name>", views.drinkItems, name="drink_name")  

    # http://127.0.0.1:8000/drinks/tea
    path("drinks/<str:drink_name>", views.drinkItems, name="drink_name")  
]
