from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import MenuItem
# from .models import Category
from .serializers import MenuItemSerializer
from django.shortcuts import get_object_or_404
# Create your views here.

# create new

class MenuItemView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

# update and delete

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


# help to selective output
@api_view()
def menu_items(request):
    # items = MenuItem.objects.select_related('category').all()
    items = MenuItem.objects.all()
    serialized_item = MenuItemSerializer(items, many = True)
    return Response(serialized_item.data)

@api_view()
def single_item(request, id):
    item = get_object_or_404(MenuItem, pk=id)
    serialized_item = MenuItemSerializer(item)
    return Response(serialized_item.data)
