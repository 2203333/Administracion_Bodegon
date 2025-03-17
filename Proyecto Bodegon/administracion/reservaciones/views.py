from django.shortcuts import render
from rest_framework import generics, viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Menus, Reservas
from .serializers import menusSerializer, reservasSerializer, UserSerializer 
from django.contrib.auth.models import User


def index(request):
    return render(request, 'index.html', {})

class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [permissions.IsAuthenticated] 

class ReservasViewSet(viewsets.ModelViewSet):
    queryset = Reservas.objects.all()
    serializer_class = reservasSerializer

class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menus.objects.all()
    serializer_class = menusSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menus.objects.all()
    serializer_class = menusSerializer