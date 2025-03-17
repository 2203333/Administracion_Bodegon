from rest_framework import serializers
from .models import Menus, Reservas
from django.contrib.auth.models import User 


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class menusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menus
        fields = '__all__'

class reservasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservas
        fields = '__all__'        