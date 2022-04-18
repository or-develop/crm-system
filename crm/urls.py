from django.urls import path

from .views import hello_view


app_name = 'crm'

urlpatterns = [
    path('v1/', hello_view, name='hello_view_url'),
]
