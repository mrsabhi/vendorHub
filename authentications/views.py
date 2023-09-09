from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate, logout

from authentications.models import User
from authentications.serializer import RegistrationSerializer, LoginSerializer


# Create your views here.

class RegistrationView(APIView):

    def get(self, request):
        user = User.objects.all()
        serializer = RegistrationSerializer(user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

            return Response({"message": "user registration successful", }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        user = User.objects.all()
        serializer = LoginSerializer(user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, requset):
        serializer = LoginSerializer(data=requset.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            # https: // docs.djangoproject.com / en / 4.2 / topics / auth / default /  # user-objects
            user = authenticate(email=email, password=password)
            if user is not None:
                return Response({"message": "user login", }, status=status.HTTP_200_OK)
            else:
                return Response({"message": "invalid email id or password"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#
class LogoutView(APIView):
    def post(self, request):
        logout(request.data)
        return Response({'message': "Logout successful"})
