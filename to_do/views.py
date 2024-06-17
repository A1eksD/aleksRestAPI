
from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers
from rest_framework import viewsets
from .serializers import TodoSerializer
from .models import toDo
import json



# import from Django REST framework
class TodoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewd or edited.
    """
    queryset = toDo.objects.all().order_by('-created_at') # orientierung an created_at
    serializer_class = TodoSerializer
    permission_classes = []
    
    
    def create(self, request): #erstellen einer create function, weil die standart function mit der serializer nicht mehr klappt
        todo = toDo.objects.create(title= request.data.get('title', ''),
                                   descrition= request.data.get('descrition', ''),
                                   user= request.user,)
        
        serialized_obj = serializers.serialize('json', [todo,])
        return HttpResponse(serialized_obj, content_type='application/json')
    