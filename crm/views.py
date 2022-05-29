from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from .permissions import IsOwnerOrReadOnly, IsAdminOrSuperuserOnly
from .models import Lead, Agent
from .services import get_all, last_requests
from .serializers import AddLeadSerializer, LeadListSerializer, AgentSerializer


class LeadViewSet(ModelViewSet):
    """ ViewSet для добавления Лида в базу и вывода всех Лидов. """
    queryset = get_all(Lead)
    serializer_class = AddLeadSerializer


class LatestRequests(ListAPIView):
    """ Класс получения заявок. """

    serializer_class = LeadListSerializer

    def get_queryset(self):
        days = self.kwargs['days']
        return last_requests(Lead, days)


class AgentViewSet(ModelViewSet):
    """ ViewSet для добавления, вывода и редактирования Агента.  """
    queryset = get_all(Agent)
    serializer_class = AgentSerializer

    def get_permissions(self):
        if self.action in ['update', 'get', ]:
            self.permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
        elif self.action in ['create']:
            self.permission_classes = (IsAdminOrSuperuserOnly, )
        return super(self.__class__, self).get_permissions()

    def retrieve(self, request, pk=None):
        agent = get_object_or_404(Agent, pk=self.kwargs['pk'])
        if not agent.phone:
            agent.phone = 'не указано'

        if not agent.date_of_birth:
            agent.date_of_birth = 'не указано'

        return Response(self.get_serializer(agent).data)
