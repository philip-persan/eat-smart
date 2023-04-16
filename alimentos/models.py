from django.db import models


class Alimento(models.Model):
    nome = models.CharField(
        verbose_name='Nome do alimento',
        max_length=50,
        blank=False,
        null=True
    )
    porcao_choices = (
        ('Unidade', 'Unidade'),
        ('Gramas', 'Gramas'),
    )
    porcao = models.CharField(
        verbose_name='Proção',
        max_length=50,
        blank=False,
        null=True,
        choices=porcao_choices
    )
    kcal = models.DecimalField(
        verbose_name='Kcal',
        max_digits=5,
        decimal_places=2,
        blank=False,
        null=True
    )
    carboidratos = models.DecimalField(
        verbose_name='Carboidratos',
        max_digits=5,
        decimal_places=2,
        blank=False,
        null=True
    )
    proteinas = models.DecimalField(
        verbose_name='Proteínas',
        max_digits=5,
        decimal_places=2,
        blank=False,
        null=True
    )
    gorduras = models.DecimalField(
        verbose_name='Gorduras',
        max_digits=5,
        decimal_places=2,
        blank=False,
        null=True
    )
    quantidade = models.DecimalField(
        verbose_name='Quantidade',
        max_digits=5,
        decimal_places=2,
        blank=False,
        null=True
    )

    @property
    def kcal_total(self):
        kcal = float(self.kcal)
        quantidade = float(self.quantidade)
        if self.porcao == 'Unidade':
            total = kcal * quantidade
            return total
        elif self.porcao == 'Gramas':
            kcal = self.kcal
            quantidade = self.quantidade
            proporcao = kcal / quantidade
            total = proporcao * quantidade
            return total

    def __str__(self) -> str:
        quantidade = round(self.quantidade)
        porcaro = self.porcao
        nome = self.nome
        frase = f'{quantidade} {porcaro} de {nome}'
        return frase

    class Meta:
        verbose_name = 'Alimento'
        verbose_name_plural = 'Alimentos'
        ordering = 'nome',
