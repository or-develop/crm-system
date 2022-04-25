from rest_framework import generics

from .models import Lead
from .services import get_all
from .serializers import *


class AddLead(generics.CreateAPIView):
    """ Класс добавления Лида в базу. """

    queryset = get_all(Lead)
    serializer_class = AddLeadSerializer


class LeadList(generics.ListAPIView):
    """ Класс вывода списка всех Лидов"""

    queryset = get_all(Lead)
    serializer_class = LeadListSerializer
