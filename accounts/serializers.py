from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

# Create endpoint for user registration, but ensure that users cannot self-register as admins
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'role')
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            role='user'  # Force role to be 'user' regardless of input
        )
        return user

# Ensure users cannot self-register as admins
class UserSerializer(serializers.Serializer):
    policy_subscriptions = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    def create(self, validated_data):
        validated_data['role'] = 'USER'
        return super().create(validated_data)