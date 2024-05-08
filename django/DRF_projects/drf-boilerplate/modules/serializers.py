from rest_framework import serializers
from .models import Module

from rest_framework_simplejwt.authentication import JWTAuthentication


class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ["id", "name", "code"]

        authentication_classes = [JWTAuthentication]
