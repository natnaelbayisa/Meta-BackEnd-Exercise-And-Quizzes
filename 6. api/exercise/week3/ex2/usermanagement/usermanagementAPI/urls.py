from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('categories', views.CategoriesView.as_view()),
    path('menu-items', views.MenuItemsView.as_view()),
    path('secret/', views.secret),
    path('api-token-auth/', obtain_auth_token),
    path('manager-view/', views.manager_view),
    path('throttle-check', views.throttle_check),
    path('throttle-auth-check', views.throttle_check_auth)
]
