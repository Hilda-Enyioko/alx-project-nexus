from rest_framework import serializers
from .models import PropertyCategory, InsurancePlan, PolicySubscription

class PropertyCategorySerializer(serializers.Serializer):
    insurance_plans = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    class Meta:
        model = PropertyCategory
        fields = '__all__'
        
class InsurancePlanSerializer(serializers.Serializer):
    policy_subscriptions = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    class Meta:
        model = InsurancePlan
        fields = '__all__'
        
class PolicySubscriptionSerializer(serializers.Serializer):
    class Meta:
        model = PolicySubscription
        fields = '__all__'