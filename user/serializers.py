from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from user.models import User
from user.regex import phone_regex


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["id", "first_name", "username", "phone_number", "password"]


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True, style={"input_type": "password"})

    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")

        if username and password:
            user = User.objects.filter(username=username).first()

            if user:
                if not user.is_active:
                    raise serializers.ValidationError("User account is disabled.")
                if not user.check_password(password):
                    raise serializers.ValidationError("Invalid password.")
            else:
                raise serializers.ValidationError("User not found.")
        else:
            raise serializers.ValidationError('Must include "username" and "password".')

        refresh = RefreshToken.for_user(user)
        attrs["tokens"] = {"access": str(refresh.access_token), "refresh": str(refresh)}
        return attrs


class SendVerificationCodeSerializer(serializers.Serializer):
    phone_number = serializers.CharField(validators=[phone_regex])
