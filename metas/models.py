from django.db import models

from users.models import User


class MetaMacro(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Usuário'
    )
    descricao = models.CharField(
        verbose_name='Descrição',
        max_length=50,
        blank=False,
        null=True
    )
    carboidratos = models.FloatField(
        verbose_name='Carboidratos',
        blank=False,
        null=True
    )
    proteinas = models.FloatField(
        verbose_name='Proteinas',
        blank=False,
        null=True
    )
    gorduras = models.FloatField(
        verbose_name='Gorduras',
        blank=False,
        null=True
    )

    def __str__(self) -> str:
        return self.descricao

    class Meta:
        verbose_name = 'Meta Macro'
        verbose_name_plural = 'Metas Macro'
