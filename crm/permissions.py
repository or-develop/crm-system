from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
    """ 
        Для ограничения доступа к агентам.
    """

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True

        return obj.pk == request.user.pk


class IsAdminOrSuperuserOnly(BasePermission):
    """
        Доступ только для админов и суперпользователя
    """

    def has_permission(self, request, obj):

        if request.user in (request.user.is_staff, request.user.is_superuser):
            return True
