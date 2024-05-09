from rest_framework import serializers

from modules.models import Module
from modules.serializers import ModuleSerializer
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    module = ModuleSerializer(read_only=True)

    class Meta:
        model = Student
        fields = [
            "id",
            "name",
            "birthday",
            "gender",
            "gpa",
            "module",
        ]


class CreateStudentSerializer(serializers.ModelSerializer):
    module_id = serializers.IntegerField()

    class Meta:
        model = Student
        fields = [
            "name",
            "birthday",
            "gender",
            "gpa",
            "module_id",
        ]

    def validate_module_id(self, value):
        try:
            Module.objects.get(id=value)
        except Module.DoesNotExist:
            raise serializers.ValidationError(
                "Module with the provided ID does not exist."
            )
        return value


class UpdateStudentSerializer(CreateStudentSerializer):
    pass
