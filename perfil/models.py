from datetime import date

from django.db import models

from users.models import User


class UserPerfil(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name='Usuário'
    )
    data_nascimento = models.DateField(
        verbose_name='Data de Nascimento',
        auto_now_add=False,
        blank=False,
        null=True
    )
    genero = models.CharField(
        verbose_name='Gênero',
        max_length=1,
        blank=False,
        null=True,
        choices=(
            ('M', 'Masculino'),
            ('F', 'Feminino'),
        )
    )
    peso_atual = models.DecimalField(
        verbose_name='Peso atual',
        max_digits=5,
        decimal_places=2,
        blank=False,
        null=True
    )
    peso_alvo = models.DecimalField(
        verbose_name='Peso alvo',
        max_digits=5,
        decimal_places=2,
        blank=False,
        null=True
    )
    altura = models.PositiveIntegerField(
        verbose_name='Altura em CM',
        blank=False,
        null=True
    )
    nivel_de_atividade = models.DecimalField(
        verbose_name='Nível de Atividade',
        max_digits=5,
        decimal_places=2,
        blank=False,
        null=True,
        help_text="0.2= Sedentário \n 0.3= Levemente Ativo \n 0.4= Moderadamente Ativo \n 0.5= Muito Ativo \n"  # noqa
    )

    def __str__(self) -> str:
        return f'{self.user.get_full_name()} - Perfil'

    @property
    def idade(self) -> int:
        ano_nascimento = self.data_nascimento.year
        ano_atual = date.today().year
        idade = ano_atual - ano_nascimento
        return idade

    @property
    def TMB(self) -> float:
        if self.genero == 'M':
            idade = float(self.idade)
            altura = float(self.altura)
            peso = float(self.peso_atual)
            tmb = 88.36 + (13.4 * peso) + (4.8 * altura) - (5.7 * idade)
            return tmb
        else:
            idade = float(self.idade)
            altura = float(self.altura)
            peso = float(self.peso_atual)
            tmb = 447.6 + (9.2 * peso) + (3.1 * altura) - (4.3 * idade)
            return tmb

    @property
    def GEAF(self) -> float:
        nivel_de_atividade = float(self.nivel_de_atividade)
        tmb = float(self.TMB)
        resultado = tmb * nivel_de_atividade
        return resultado

    @property
    def GET(self) -> float:
        if self.genero == 'M':
            geb = float(self.TMB)
            geaf = float(self.GEAF)
            nivel_de_atividade = float(self.nivel_de_atividade)
            get = (geb * 1.2) + (geaf * nivel_de_atividade)
            return get
        else:
            geb = float(self.TMB)
            geaf = float(self.GEAF)
            nivel_de_atividade = float(self.nivel_de_atividade)
            get = (geb * 0.9) + (geaf * nivel_de_atividade)
            return get

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'
