from django.db.models.base import Model
from django.db.models import QuerySet
import datetime


def get_all(model: Model) -> QuerySet:
    """
        Возвращает QuerySet с результатом выборки всех атрибутов модели.
    """

    return model.objects.all()


def last_thirty_days(model: Model) -> QuerySet:
    """ Возвращает QuerySet с последними заявками за 30 дней. """

    days_ago = datetime.date.today() - datetime.timedelta(days=30)

    return model.objects.filter(created__gte=days_ago)
