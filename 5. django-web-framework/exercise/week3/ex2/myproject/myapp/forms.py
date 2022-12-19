from django import forms 
from django.http import HttpResponse

class DemoForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=10)
    


def user_form(request):
    # new_form = DemoForm()
    return HttpResponse(DemoForm())