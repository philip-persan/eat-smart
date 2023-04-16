from django.db import models
from django.db.models import Sum

from alimentos.models import Alimento


class Refeicao(models.Model):
    descricao = models.CharField(
        verbose_name='Descrição',
        max_length=70,
        blank=False,
        null=True
    )
    alimentos = models.ManyToManyField(
        Alimento,
        verbose_name='Alimentos'
    )

    @property
    def total_kcal(self):
        kcal = self.alimentos.aggregate(total=Sum('kcal'))
        return kcal.get('total')

    @property
    def total_carboidratos(self):
        carboidratos = self.alimentos.aggregate(total=Sum('carboidratos'))
        return carboidratos.get('total')

    @property
    def total_proteinas(self):
        proteinas = self.alimentos.aggregate(total=Sum('proteinas'))
        return proteinas.get('total')

    @property
    def total_gorduras(self):
        gorduras = self.alimentos.aggregate(total=Sum('gorduras'))
        return gorduras.get('total')

    def __str__(self) -> str:
        return self.descricao

    class Meta:
        verbose_name = 'Refeição'
        verbose_name_plural = 'Refeições'
