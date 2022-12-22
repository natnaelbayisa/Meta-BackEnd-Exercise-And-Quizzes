
from django.urls import path
from . import views

urlpatterns = [
    path("", views.sth),
    path("home/", views.form_view),
    path("login/", views.login_form)
]
