from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    InsurancePlanViewSet,
    PropertyCategoryViewSet,
    PolicySubscriptionViewSet
)

router = DefaultRouter()
router.register(r'insurance-plans', InsurancePlanViewSet, basename='insurance-plan')
router.register(r'property-categories', PropertyCategoryViewSet, basename='property-category')
router.register(r'policy-subscriptions', PolicySubscriptionViewSet, basename='policy-subscription')

urlpatterns = [
    path('', include('router.urls'))
]