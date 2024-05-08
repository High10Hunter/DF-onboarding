from .models import Module
from .serializers import ModuleSerializer
from rest_framework import viewsets, mixins


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

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.serializers["default"])
