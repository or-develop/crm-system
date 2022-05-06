from rest_framework import generics

from .models import Lead
from .services import get_all, last_requests
from .serializers import AddLeadSerializer, LeadListSerializer


class AddLead(generics.CreateAPIView):
    """ Класс добавления Лида в базу. """

    queryset = get_all(Lead)
    serializer_class = AddLeadSerializer


class LeadList(generics.ListAPIView):
    """ Класс вывода списка всех Лидов"""

    queryset = get_all(Lead)
    serializer_class = LeadListSerializer


class LatestRequests(generics.ListAPIView):
    """ Класс получения заявок. """

    serializer_class = LeadListSerializer

    def get_queryset(self):
        days = self.kwargs['days']
        return last_requests(Lead, days['days'])
