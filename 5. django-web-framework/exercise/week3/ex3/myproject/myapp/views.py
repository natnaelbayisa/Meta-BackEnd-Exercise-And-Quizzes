from django.shortcuts import render
from django.http import HttpResponse
from myapp.forms import InputForm
from myapp.forms import LogForm

from django.core.exceptions import PermissionDenied  
# Create your views here.

def form_view(request):
    form = InputForm()
    context = {"form":form}
    return render(request, "home.html", context)


def login_form(request):
    loginForm = LogForm()
    
    if request.method == "POST":
        form = LogForm(request.POST)
        
        if form.is_valid():
            form.save()
    
    context = {"form": loginForm}
    return render(request, "home.html", context)


def myview(request): 
    if request.user.is_anonymous(): 
        raise PermissionDenied() 

def sth(request):
    return render(request, 'base.html')