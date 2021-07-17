from django.conf import settings
from django.contrib.auth import authenticate
from rest_framework.generics import GenericAPIView
from rest_framework import permissions, status

from authentication.serializers import RegisterSerializer, LoginSerializer
from lib.response import Response

import jwt


class RegisterView(GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(errors=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        data = request.data
        username = data.get('username', '')
        password = data.get('password', '')

        user = authenticate(username=username, password=password)
        
        if user:
            auth_token = jwt.encode(
                {'username': username}, settings.JWT_SECRET_KEY)

            serializer = self.get_serializer(user)

            data = {
                'user': serializer.data,
                'token': auth_token,
            }
            return Response(data=data, status=status.HTTP_200_OK)
        return Response(errors={'detail':'Invalid credentials. Ensure both username and password are correct'}, status=status.HTTP_401_UNAUTHORIZED)
