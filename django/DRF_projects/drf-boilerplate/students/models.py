from django.db import models

from modules.models import Module


class Student(models.Model):
    name = models.CharField(max_length=100)
    birthday = models.DateField()
    gender = models.BooleanField(default=True)
    gpa = models.FloatField()
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
