from django.urls import path

from .views import AddLead


app_name = 'crm'

urlpatterns = [
    path('add_lead/', AddLead.as_view(), name='add_lead_url')
]
