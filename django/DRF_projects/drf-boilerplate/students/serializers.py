from rest_framework import serializers
from .models import Student

from rest_framework_simplejwt.authentication import JWTAuthentication


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            "id",
            "name",
            "birthday",
            "gender",
            "gpa",
            "module_id",
        ]

    authentication_classes = [JWTAuthentication]
