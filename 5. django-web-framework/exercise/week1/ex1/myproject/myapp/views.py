from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

# def home(request):
#     return HttpResponse("Welcome to my django site")


def home(request):
    content = "<html><body><h1>Welcome to my page</h1></body></html`"
    return HttpResponse(content)