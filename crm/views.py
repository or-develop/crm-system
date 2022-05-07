from rest_framework import generics, viewsets
from .models import Lead, Agent
from .services import get_all, IsOwnerOrReadOnly
from .serializers import AddLeadSerializer, LeadListSerializer, AgentSerializer


class AddLead(generics.CreateAPIView):
    """ Класс добавления Лида в базу. """

    queryset = get_all(Lead)
    serializer_class = AddLeadSerializer


class LeadList(generics.ListAPIView):
    """ Класс вывода списка всех Лидов"""

    queryset = get_all(Lead)
    serializer_class = LeadListSerializer


class AgentList(viewsets.ModelViewSet):
    """ Класс вывода и редактирования всех агентов. """

    queryset = get_all(Agent)
    serializer_class = AgentSerializer
    permission_classes = [IsOwnerOrReadOnly]
