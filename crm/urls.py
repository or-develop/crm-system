from django.urls import path
from .views import AddLead, LeadList, AgentList


app_name = 'crm'

urlpatterns = [
    path('add_lead/', AddLead.as_view(), name='add_lead_url'),
    path('leads/', LeadList.as_view(), name='list_lead_url'),
    path('agents/', AgentList.as_view({'get': 'list'}), name='list_agent_url'),
    path('agent/update/<int:pk>/',
         AgentList.as_view({'get': 'retrieve', 'put': 'update'}), name='update_agent_url'),
]
