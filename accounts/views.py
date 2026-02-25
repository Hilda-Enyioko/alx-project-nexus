from django.shortcuts import render
from .serializers import RegisterSerializer, CustomTokenObtainPairSerializer
from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView

# create register view for user registration
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = []  # Allow anyone to access this view for registration
    
# create a custom view for jwt tokens
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer