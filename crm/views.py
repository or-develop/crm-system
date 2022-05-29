from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action

from .permissions import IsOwnerOrReadOnly
from .models import Lead, Agent
from .services import last_requests
from .serializers import LeadSerializer, AgentSerializer


class LeadViewSet(viewsets.ModelViewSet):
    """" Класс Лида """
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

    @action(methods=['get'], detail=False)
    def last_requests(self):
        days = self.kwargs['days']
        return last_requests(Lead, days)


class AgentViewSet(viewsets.ModelViewSet):
    """Класс Агента"""

    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
