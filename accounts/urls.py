from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path("login/", TokenObtainPairView.as_view(), name = "login"),
    path("token/refresh", TokenObtainPairView.as_view(), name="token_refresh"),
]