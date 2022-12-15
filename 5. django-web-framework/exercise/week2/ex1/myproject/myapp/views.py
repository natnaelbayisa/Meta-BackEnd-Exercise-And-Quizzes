from django.http import HttpResponse
from django.shortcuts import render
from http.client import HTTPResponse


# Create your views here.

response = HttpResponse()
response.headers["Age"] = 20

def home(request):
    path = request.path
    scheme = request.scheme
    method = request.method
    address = request.META['REMOTE_ADDR']
    user_agent = request.META["HTTP_USER_AGENT"]
    path_info = request.path_info
    
    msg = f"""<br>
        <br>Path: {path}
        <br>Address: {address}
        <br>Scheme: {scheme}
        <br>Method: {method}
        <br>User agent: {user_agent}
        <br>Path info: {path_info}
        <br>Response headers: {response.headers}
    """
    
    return HttpResponse(msg,content_type="text/html", charset="utf-8")

# render foodItems
def foodItems(request, dish):
    items = {
        "pasta": "Pasta is a type of noodle",
        "falafel": "Falafel are deep fried patties",
        "cheesecake": "Cheesecake is a type of dessert"
    }
    
    description = items[dish]
    return HttpResponse(f"<h2> {dish} </h2>" + description)

# render drinkItems
def drinkItems(request, drink_name):
    drink = {
        'mocha' : 'type of coffee',
        'tea' : 'type of hot beverage',
        'lemonade': 'type of refreshment',
    }
    
    choice_of_drink = drink[drink_name]
    
    return HttpResponse(f"<h2> {drink_name} </h2>" + choice_of_drink)