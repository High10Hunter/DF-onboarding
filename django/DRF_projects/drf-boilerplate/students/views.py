from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets, mixins

from rest_framework.permissions import IsAuthenticated


class StudentsApiView(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Student.objects.all()
    serializers = {"default": StudentSerializer}
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.serializers["default"])
