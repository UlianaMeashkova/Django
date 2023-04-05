from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from api.users.serializers import RegisterSerializer, LoginSerializer


class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User(
            email=serializer.validated_data["email"],
            username=serializer.validated_data["email"],
        )
        user.set_password(serializer.validated_data["password"])
        user.save()
        return Response(status=status.HTTP_201_CREATED)


class LoginView(CreateAPIView):
    serializer_class = LoginSerializer
    permission_classes = []

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(
            request=request,
            username=serializer.validated_data["email"],
            password=serializer.validated_data["password"],
        )
        if user is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        token = Token.objects.get_or_create(user=user)[0].key
        return Response(status=status.HTTP_200_OK, data={"token": token})