from rest_framework import generics
from .models import MenuItem, Category
from .serializers import MenuItemSerializer, CategorySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes, throttle_classes
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from .throttles import TenCallsPerMinute


class CategoriesView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    ordering_fields = ['price', 'inventory']
    filterset_fields = ['price', 'inventory']
    search_fields = ['title']


#  give access to only authenticated users
@api_view()
@permission_classes([IsAuthenticated])
def secret(request):
    return Response({"message": "This message is secret"})

# display a message only for manager
@api_view()
@permission_classes([IsAuthenticated])
def manager_view(request):
    if request.user.groups.filter(name = 'Manager').exists():
        return Response({'message': 'only manager should see this'})
    else:
        return Response({'message': 'you are not authorized'}, 403)


# Limiting user access
@api_view()
@throttle_classes([AnonRateThrottle])
def throttle_check(request):
    return Response({'message':'successful'})


@api_view()
@permission_classes([IsAuthenticated])
@throttle_classes([TenCallsPerMinute])

def throttle_check_auth(request):
    return Response({'message':'message for logged inuser only'})
