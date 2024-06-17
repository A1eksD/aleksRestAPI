from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from .models import toDo

# Serializers define the API representation.
# import from Django REST framework
class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = toDo
        fields = ['id','title', 'descrition', 'created_at']
