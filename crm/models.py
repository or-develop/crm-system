from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import AgentManager


class AbstractModelDateTime(models.Model):
    """ 
        Абстрактная модель определяющая поля datetimefield для других моделей. 
        updated - Поле последнего обновления;
        created - Поле создания записи.
    """

    updated = models.DateTimeField('Обновлено', auto_now=True)
    created = models.DateTimeField('Создано', auto_now_add=True)

    class Meta:
        abstract = True


class Agent(AbstractUser):
    """ Кастомная модель пользователя в системе. """

    username = None

    email = models.EmailField('Email', max_length=256,
                              unique=True, blank=False)

    first_name = models.CharField('Имя', max_length=256, blank=False)
    last_name = models.CharField('Фамилия', max_length=256, blank=False)

    phone = models.CharField(
        'Номер телефона', max_length=50, blank=True, unique=True)
    date_of_birth = models.DateField(
        'Дата рождения', auto_now=False, auto_now_add=False, blank=True, null=True)

    success_deal = models.PositiveIntegerField('Успешных сделок', default=0)
    fail_deal = models.PositiveIntegerField('Провальных сделок', default=0)

    objects = AgentManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name} [{self.email}]'

    class Meta:
        verbose_name = 'Агент'
        verbose_name_plural = 'Агенты'
        db_table = 'agents'


class Lead(AbstractModelDateTime):
    """ Модель потенциального клиента. """

    updated = None

    name = models.CharField('Имя клиента', max_length=256)
    email = models.EmailField('Email клиента', max_length=256)
    phone = models.CharField('Номер телефона клиента',
                             max_length=50, blank=True)

    def __str__(self) -> str:

        string_representation = f'Потенциальный клиент {self.name} ({self.email})'

        if self.phone:
            return string_representation + f' ({self.phone})'

        return string_representation

    class Meta:
        verbose_name = 'Потенциальный клиент'
        verbose_name_plural = 'Потенциальные клиенты'
        db_table = 'leads'
