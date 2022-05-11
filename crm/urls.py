from django.urls import path

from .views import AddLead, LeadList, LatestRequests, AgentList, AddAgent


app_name = 'crm'

urlpatterns = [
    path('add_lead/', AddLead.as_view(), name='add_lead_url'),
    path('leads/', LeadList.as_view(), name='list_lead_url'),
    path('latest_requests/<int:days>/', LatestRequests.as_view(), name='latest_requests_url'),
    path('agent/<int:pk>/', AgentList.as_view(), name='agent_url'),
    path('add_agent/', AddAgent.as_view(), name='add_agent_url'),
]
