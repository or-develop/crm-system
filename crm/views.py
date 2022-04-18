from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def hello_view(request) -> Response:
    """ Тестовая вьюшка - удалить при разработке. """

    if request.method == 'GET':
        return Response(
            {'success': True, 'msg': 'Hello World!'},
            status=status.HTTP_200_OK)
