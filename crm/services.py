from django.db.models.base import Model
from django.db.models import QuerySet


def get_all(model: Model) -> QuerySet:
    """
        Возвращает QuerySet с результатом выборки всех атрибутов модели.
    """

    return model.objects.all()