from django.urls import path
from . import views

urlpatterns = [
    # path('books/', views.book, name="book")
    path('books/', views.BookList.as_view()),
    path('books/<int:pk>', views.Book.as_view())
]