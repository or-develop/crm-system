import datetime
from django.db.models.base import Model
from django.db.models import QuerySet


def last_requests(model: Model, days: int) -> QuerySet:
    """ Возвращает QuerySet с последними заявками за выбранную дату """

    days_ago = datetime.date.today() - datetime.timedelta(days=days)
    return model.objects.filter(created__gte=days_ago)
