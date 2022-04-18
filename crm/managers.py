from django.contrib.auth.models import User
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class AgentManager(BaseUserManager):
    """ Кастомный менеджер модели для пользователя. """

    def create_user(self, email: str, password: str, **extra_fields: dict) -> User:
        """ Создаёт обычного пользователя. """

        if not email:
            raise ValueError(_('The Email must be set'))

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email: str, password: str, **extra_fields: dict) -> User:
        """ Создаёт супер-пользователя. """

        superuser_flags = (
            'is_staff',
            'is_superuser',
            'is_active',
        )

        extra_fields.update(
            **dict.fromkeys(superuser_flags, True)
        )

        for flag in superuser_flags:
            self.validate_superuser(extra_fields, flag)

        return self.create_user(email, password, **extra_fields)

    @staticmethod
    def validate_superuser(sequence: dict, flag: str) -> None:
        """ 
            Валидация супер-пользователя. Возбуждает исключение если параметр flag не установлен в значение True. 
        """

        if sequence.get(flag) is not True:
            raise ValueError(_(f'Superuser must have {flag}=True.'))
