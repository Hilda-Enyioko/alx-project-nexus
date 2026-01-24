from django.db import models
from accounts.models import User

class PropertyCategory(models.Model):
    PROPERTY_NAMES = [
        ('apartment', 'Apartment'),
        ('house', 'House'),
        ('duplex', 'Duplex'),
        ('bungalow', 'Bungalow'),
        ('small-commercial', 'Small Commercial')
    ]
    
    name = models.TextField(choices=PROPERTY_NAMES, unique=True)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)


# Core e-commerce product
class InsurancePlan(models.Model):
    COVERAGE_LEVELS = [
        ('basic', 'Basic'),
        ('standard', 'Standard'),
        ('premium', 'Premium')
    ]
    
    name = models.CharField(max_length=500)
    property_category = models.ForeignKey(PropertyCategory, on_delete=models.CASCADE, db_index=True)
    coverage_level = models.TextField(choices=COVERAGE_LEVELS, db_index=True)
    coverage_amount = models.DecimalField(max_digits=20, decimal_places=2)
    premium = models.DecimalField(max_digits=20, decimal_places=2, db_index=True)
    duration_months = models.IntegerField()
    description = models.TextField()
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


# Basically the e-commerce order placed
class PolicySubscription(models.Model):
    POLICY_STATUSES = [
        ('active', 'Active'),
        ('expired', 'Expired'),
        ('cancelled', 'Cancelled')
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)
    insurance_plan = models.ForeignKey(InsurancePlan, on_delete=models.CASCADE, db_index=True)
    start_date = models.DateField(db_index=True)
    end_date = models.DateField(db_index=True)
    status = models.TextField(choices=POLICY_STATUSES, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)