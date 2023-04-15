import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    id = models.UUIDField(
        verbose_name='id',
        primary_key=True,
        editable=False,
        default=uuid.uuid4
    )
    email = models.EmailField(
        verbose_name='email',
        unique=True,
        blank=False,
        null=True
    )
    telefone = models.CharField(
        verbose_name='Telefone',
        max_length=11,
        blank=False,
        null=True,
        unique=True
    )

    def save(self, *args, **kwargs):
        self.username = self.email
        return super().save(args, kwargs)

    def __str__(self) -> str:
        return self.get_full_name()

    USERNAME_FIELD: str = 'email'
    REQUIRED_FIELDS = ['telefone', 'username']

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
