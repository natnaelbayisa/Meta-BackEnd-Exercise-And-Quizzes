from django.http import HttpResponse, HttpResponseNotFound

def handler404(request, exception):
    return HttpResponse("404: Page not found! <br><br> <button onclick="" href='';"">Go to Homepage</button>")

def test(request):
    return HttpResponseNotFound("WELCOME *")