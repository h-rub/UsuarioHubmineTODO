from unicodedata import name
from django.db import models


# Create your models here.

class Usuarios(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class Priority(models.Model):
    priorityName = models.CharField(max_length=50)

class Tasks(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    dead_line = models.DateField()
    isCompleted = models.BooleanField()
    priority_id = models.ForeignKey(Priority, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

