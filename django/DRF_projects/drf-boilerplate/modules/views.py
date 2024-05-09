from rest_framework.pagination import LimitOffsetPagination

from utils.pagination.custorm_pagination import CustomPagination
from .models import Module
from .serializers import ModuleSerializer
from rest_framework import viewsets, mixins

from rest_framework.permissions import IsAuthenticated


class ModulesApiView(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Module.objects.all()
    serializers = {"default": ModuleSerializer}
    # pagination_class = LimitOffsetPagination
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.serializers["default"])
