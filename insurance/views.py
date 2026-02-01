from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import IsAdminRole, IsUserRole
from .models import InsurancePlan, PropertyCategory, PolicySubscription
from .serializers import InsurancePlanSerializer, PropertyCategorySerializer, PolicySubscriptionSerializer
from drf_spectacular.utils import extend_schema

class InsurancePlanViewSet(ModelViewSet):
    # Query optimization
    queryset = InsurancePlan.objects.prefetch_related('policy_subscriptions')
    serializer_class = InsurancePlanSerializer

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAdminRole()]
        return [IsAuthenticated()]
    
    @extend_schema(
        summary="List all insurance plans",
        description="Returns a paginated list of insurance plans"
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    
class PropertyCategoryViewSet(ModelViewSet):
    queryset = PropertyCategory.objects.all()
    serializer_class = PropertyCategorySerializer

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAdminRole()]
        return [IsAuthenticated()]

    
    @extend_schema(
        summary="List all property category",
        description="Returns a paginated list of property category"
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
 
    
class PolicySubscriptionViewSet(ModelViewSet):
    serializer_class = PolicySubscriptionSerializer

    def get_queryset(self):
        # Users can only see their own policy subscriptions and related insurance plans
        return PolicySubscription.objects.select_related("insurance_plan", "user").filter(user=self.request.user)


    def get_permissions(self):
        if self.action == "create":
            return [IsUserRole()]
        return [IsAuthenticated()]


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
    @extend_schema(
        summary="List all policy subscription",
        description="Returns a paginated list of policy subscription"
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

