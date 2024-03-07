from django.shortcuts import render
from django.views import View
from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView, ListAPIView
from .serializers import MenuSerializer, BookingSerializer, UserSerializer, User
from .models import Menu, Booking
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class MenuItemsView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer