import datetime
from django.db import models
from django.contrib.auth.models import User



class toDo(models.Model):
    title = models.CharField(max_length=30)
    descrition = models.CharField(max_length=60)
    created_at = models.DateField(default=datetime.date.today)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        default=None
    )