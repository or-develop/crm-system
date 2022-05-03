from rest_framework import generics

from .models import Lead
from .services import get_all, last_thirty_days
from .serializers import AddLeadSerializer, LeadListSerializer, LatestApplicationsSerializer


class AddLead(generics.CreateAPIView):
    """ Класс добавления Лида в базу. """

    queryset = get_all(Lead)
    serializer_class = AddLeadSerializer


class LeadList(generics.ListAPIView):
    """ Класс вывода списка всех Лидов"""

    queryset = get_all(Lead)
    serializer_class = LeadListSerializer


class LatestApplications(generics.ListAPIView):
    """ Класс получения заявок последних 30-ти дней. """

    queryset = last_thirty_days(Lead)
    serializer_class = LatestApplicationsSerializer
