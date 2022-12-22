from django import forms 
from .models import Logger


SHIFTS = (
    ("1", "Morning"),
    ("2", "Afternoon"),
    ("3", "Evening")
)

class InputForm(forms.Form): 
    first_name = forms.CharField(label='Name of Applicant', max_length=50, required=False) 
    last_name = forms.CharField(label='Name of Applicant', max_length=50) 
    address = forms.CharField(label='Address', max_length=100) 
    shift = forms.ChoiceField(choices=SHIFTS) 
    time_log = forms.TimeField(help_text= "Enter the exact time") 

class LogForm(forms.ModelForm):
    class Meta:
        model = Logger
        fields = '__all__'