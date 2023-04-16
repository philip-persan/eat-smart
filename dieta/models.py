from django.db import models

from metas.models import MetaMacro
from perfil.models import UserPerfil


class Dieta(models.Model):
    user = models.ForeignKey(
        UserPerfil,
        on_delete=models.CASCADE,
        verbose_name='Usuário',
        blank=False,
        null=True
    )
    macros = models.ForeignKey(
        MetaMacro,
        on_delete=models.CASCADE,
        verbose_name='Macros',
        blank=False,
        null=True
    )
    qtd_refeicoes = models.PositiveIntegerField(
        verbose_name='Quantidade de refeições',
        blank=False,
        null=True
    )

    @property
    def kcal_total(self):
        kcal = self.user.GET
        return kcal

    @property
    def carbo_total(self):
        carbo = float(self.macros.carboidratos)
        peso = float(self.user.peso_atual)
        total = carbo * peso
        return total

    @property
    def carbo_por_refeicao(self):
        carbo = float(self.carbo_total)
        qtd = float(self.qtd_refeicoes)
        total = carbo / qtd
        return total

    @property
    def proteina_total(self):
        proteina = float(self.macros.proteinas)
        peso = float(self.user.peso_atual)
        total = proteina * peso
        return total

    @property
    def proteina_por_refeicao(self):
        proteina = float(self.proteina_total)
        qtd = float(self.qtd_refeicoes)
        total = proteina / qtd
        return total

    @property
    def gordura_total(self):
        gordura = float(self.macros.gorduras)
        peso = float(self.user.peso_atual)
        total = gordura * peso
        return total

    @property
    def gordura_por_refeicao(self):
        gorudra = float(self.gordura_total)
        qtd = float(self.qtd_refeicoes)
        total = gorudra / qtd
        return total

    def __str__(self) -> str:
        return f'{self.user.user.first_name} - Dieta'

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Dieta'
        verbose_name_plural = 'Dietas'
