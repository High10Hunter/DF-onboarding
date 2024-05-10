from rest_framework.pagination import LimitOffsetPagination

from utils.pagination.custorm_pagination import CustomPagination
from .models import Student
from .serializers import (
    CreateStudentSerializer,
    StudentSerializer,
    UpdateStudentSerializer,
)
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
    serializers = {
        "default": StudentSerializer,
        "create": CreateStudentSerializer,
        "update": UpdateStudentSerializer,
        "partial_update": UpdateStudentSerializer,
    }
    # pagination_class = LimitOffsetPagination
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.serializers["default"])

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)
