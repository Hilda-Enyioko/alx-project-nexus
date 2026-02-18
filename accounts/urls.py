from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("login/", TokenObtainPairView.as_view(), name = "login"),
    path("token/refresh", TokenRefreshView.as_view(), name="token_refresh"),
]