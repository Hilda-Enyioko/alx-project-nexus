from rest_framework import serializers

# Ensure users cannot self-register as admins
class UserSerializer(serializers.Serializer):
    policy_subscriptions = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    def create(self, validated_data):
        validated_data['role'] = 'USER'
        return super().create(validated_data)