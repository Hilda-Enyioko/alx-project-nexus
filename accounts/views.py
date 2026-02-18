from django.shortcuts import render
from .serializers import RegisterSerializer
from rest_framework import generics

# create register view for user registration
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = []  # Allow anyone to access this view for registration