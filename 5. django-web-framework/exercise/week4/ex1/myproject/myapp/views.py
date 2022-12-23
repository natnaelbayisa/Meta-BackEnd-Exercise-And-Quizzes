from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse 
def about(request): 
    about_content = {'about': "History of Lorem Ipsum originates with Cicero in the 1st Century BC and his text De Finibus bonorum et malorum. This philosophical work, also known as On the Ends of Good and Evil, was split into five books."}
    return render(request, "about.html",  about_content) 