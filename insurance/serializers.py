from rest_framework import serializers
from datetime import date, timedelta
from .models import PropertyCategory, InsurancePlan, PolicySubscription

class PropertyCategorySerializer(serializers.ModelSerializer):
    insurance_plans = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    class Meta:
        model = PropertyCategory
        fields = '__all__'
        
class InsurancePlanSerializer(serializers.ModelSerializer):
    policy_subscriptions = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    class Meta:
        model = InsurancePlan
        fields = '__all__'
        
    # Validate insurance plan duration
    def validate(self, attrs):
        duration_months = attrs.get("duration_months")
        if duration_months is None or duration_months < 1 or duration_months % 6 != 0:
            raise serializers.ValidationError(
                "Insurance plan duration must be at least 1 month and in multiples of 6 months."
            )
        return attrs
        
class PolicySubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PolicySubscription
        fields = '__all__'
        read_only_fields = ('end_date',)
        
    # Validate start date
    def validate(self, attrs):
        start_date = attrs.get("start_date")
            
        min_start_date = date.today() + timedelta(days=7)
        if start_date < min_start_date:
            raise serializers.ValidationError(
                "Policy start date must be at least 7 days from today."
            )
        
        return attrs
    
    def create(self, validated_data):
        insurance_plan = validated_data["insurance_plan"]
        start_date = validated_data["start_date"]
        
        validated_data["end_date"] = (
            start_date + timedelta(days=30 * insurance_plan.duration_months)
        )
 
        return super().create(validated_data)