from rest_framework import serializers


class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(min_length=8)


class LoginSerializer(RegisterSerializer):
    """Login serializer."""