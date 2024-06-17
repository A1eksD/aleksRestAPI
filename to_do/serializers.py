from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from rest_framework.fields import CurrentUserDefault
from .models import toDo

# Serializers define the API representation.
# import from Django REST framework

class UserSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'username']

class TodoSerializer(serializers.HyperlinkedModelSerializer):
    
    # user = CurrentUserDefault()
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = toDo
        fields = ['id','title', 'descrition', 'created_at', 'user', 'time_passed']
