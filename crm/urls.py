from django.urls import path
from .views import LeadViewSet, LatestRequests, AgentViewSet


app_name = 'crm'


urlpatterns = [
    path('add_lead/',
         LeadViewSet.as_view({'post': 'create'}), name='add_lead_url'),
    path('leads/', LeadViewSet.as_view({'get': 'list'}), name='list_lead_url'),
    path('latest_requests/<int:days>/',
         LatestRequests.as_view(), name='latest_requests_url'),
    path('add_agent/',
         AgentViewSet.as_view({'post': 'create'}), 'add_agent_url'),
    path('agent/<int:pk>/',
         AgentViewSet.as_view({'put': 'update', 'get': 'retrieve'}), 'agent_url'),
]
