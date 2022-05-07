from django.db.models.base import Model
from django.db.models import QuerySet
from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(BasePermission):
    """ 
        Для ограничения доступа к агентам.
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and obj.pk == request.user.pk


def get_all(model: Model) -> QuerySet:
    """
        Возвращает QuerySet с результатом выборки всех атрибутов модели.
    """

    return model.objects.all()
