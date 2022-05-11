from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from .permissions import IsOwnerOrReadOnly, IsAdminOrSuperuserOnly
from .models import Lead, Agent
from .services import get_all, last_requests
from .serializers import AddLeadSerializer, LeadListSerializer, AgentSerializer


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
        return last_requests(Lead, days)


class AgentList(generics.RetrieveUpdateAPIView):
    """ Класс вывода и редактирования агента. """

    serializer_class = AgentSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_object(self):
        agent = get_object_or_404(Agent, pk=self.kwargs['pk'])

        if not agent.phone:
            agent.phone = 'не указано'

        if not agent.date_of_birth:
            agent.date_of_birth = 'не указано'

        return agent


class AddAgent(generics.CreateAPIView):
    """Класс добавления Агента"""

    queryset = get_all(Agent)
    serializer_class = AgentSerializer
    permission_classes = (IsAdminOrSuperuserOnly, )
