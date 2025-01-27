from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.decorators import api_view
from .models import Menu, Booking
from .serializers import MenuItemSerializer, BookingSerializer

# Create your views here.
def index(request):
    return render(request, 'index.html')

class MenuItemList(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer
    
class MenuItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    #permission_classes = [permissions.IsAuthenticated]