from django.contrib.auth import login
from django.contrib.auth.hashers import make_password
from rest_framework import generics, status
from rest_framework.response import Response

from user.serializers import UserLoginSerializer, UserSerializer, SendVerificationCodeSerializer


class UserRegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        password = serializer.validated_data["password"]
        hashed_password = make_password(password)
        serializer.save(password=hashed_password)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserLoginAPIView(generics.GenericAPIView):
    authentication_classes = []
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        tokens = serializer.validated_data["tokens"]
        response_data = {"tokens": tokens}

        return Response(response_data)


class SendVerificationCodeView(generics.CreateAPIView):
    serializer_class = SendVerificationCodeSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        phone_number = serializer.validated_data.get("phone_number")
        code = 1234  # send_verification_code(phone_number)

        return Response({"phone": phone_number, "code": code}, status=status.HTTP_201_CREATED)
