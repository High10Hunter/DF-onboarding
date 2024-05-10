from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from users.serializers import SignUpSerializer


class SignUpApiView(viewsets.GenericViewSet):
    serializer_class = SignUpSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
