from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions

from .serializers import TodoSerializer
from .models import toDo

# import from Django REST framework
class TodoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewd or edited.
    """
    queryset = toDo.objects.all().order_by('-created_at')
    serializer_class = TodoSerializer
    permission_classes = []