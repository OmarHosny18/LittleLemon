from django.shortcuts import render
from rest_framework import generics
from .models import Booking, Menu
from .serializers import BookingSerializer, MenuSerializer
from rest_framework import viewsets

# Create your views here.

def index(request):
    return render(request, 'index.html')




class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer



class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer



   