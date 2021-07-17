from rest_framework import serializers
from django.contrib.auth.models import User


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=40, min_length=8, write_only=True)
    email = serializers.EmailField()
    first_name = serializers.CharField(min_length=3, max_length=100)
    last_name = serializers.CharField(min_length=3, max_length=100)

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')

    def validate(self, attrs):
        if User.objects.filter(username=attrs['username']).exists():
            raise serializers.ValidationError({"username":
                                               "A user with that username already exists"})
        if User.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError({"email":
                                               "A user with that email already exists"})
        return super().validate(attrs)

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=40, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password')
