from django.urls import path

from .views import hello_view, AddLead


app_name = 'crm'

urlpatterns = [
    path('v1/', hello_view, name='hello_view_url'),
    path('add_lead/', AddLead.as_view(), name='add_lead')
]
