from django.urls import path

from .views import *


app_name = 'crm'

urlpatterns = [
    path('add_lead/', AddLead.as_view(), name='add_lead_url'),
    path('leads/', LeadList.as_view(), name='list_lead_url')
]
