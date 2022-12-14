from django.shortcuts import render
from django.http import HttpResponse

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