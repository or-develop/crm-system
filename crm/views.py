from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics

from .models import Lead
from .serializers import AddLeadSerializer


@api_view(['GET'])
def hello_view(request) -> Response:
    """ Тестовая вьюшка - удалить при разработке. """

    if request.method == 'GET':
        return Response(
            {'success': True, 'msg': 'Hello World!'},
            status=status.HTTP_200_OK)


class AddLead(generics.CreateAPIView):
    "Класс добавления Лида в базу"

    queryset = Lead.objects.all()
    serializer_class = AddLeadSerializer
