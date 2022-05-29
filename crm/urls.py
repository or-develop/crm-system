from django.urls import path, include

from .views import LeadViewSet, AgentViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'lead', LeadViewSet)
router.register(r'agent', AgentViewSet)

app_name = 'crm'

urlpatterns = [
    path('', include(router.urls)),
]
