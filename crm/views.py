from rest_framework import generics

from .models import Lead
from .services import get_all
from .serializers import AddLeadSerializer


class AddLead(generics.CreateAPIView):
    """ Класс добавления Лида в базу. """

    queryset = get_all(Lead)
    serializer_class = AddLeadSerializer
