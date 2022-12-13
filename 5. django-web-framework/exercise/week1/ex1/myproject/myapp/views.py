from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.


def home(request):
    return HttpResponse("Welcome to my django site")


def say_hello(request):
    content = "<html><body><h1>Welcome new comers</h1></body></html"
    return HttpResponse(content)

def displayDate(request):
    date_joined = datetime.today().year
    return HttpResponse(date_joined)

def menu(request):
    text = """
    <h1 style="color:#f4ce14;"> this is my site</h1>
    """
    return HttpResponse(text)

def welcome(request):
    welcome_text = """<h1 style="color:#f4ce14;"> Welcome  Back</h1>"""
    return HttpResponse(welcome_text)