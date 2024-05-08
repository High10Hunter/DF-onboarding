from django.db import models
from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    birthday = models.DateField()
    gender = models.BooleanField(default=True)
    gpa = models.FloatField()
    module_id = models.ForeignKey("modules.Module", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
