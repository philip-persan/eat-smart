# Generated by Django 4.2 on 2023-04-15 21:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPerfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_nascimento', models.DateField(null=True, verbose_name='Data de Nascimento')),
                ('genero', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=1, null=True, verbose_name='Gênero')),
                ('peso_atual', models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='Peso atual')),
                ('peso_alvo', models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='Peso atual')),
                ('altura', models.PositiveIntegerField(null=True, verbose_name='Altura em CM')),
                ('nivel_de_atividade', models.DecimalField(choices=[(0.2, 'Sedentário'), (0.3, 'Levemente Ativo'), (0.4, 'Moderadamente Ativo'), (0.5, 'Muito Ativo')], decimal_places=2, max_digits=5, null=True, verbose_name='Nível de Atividade')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Perfil',
                'verbose_name_plural': 'Perfis',
            },
        ),
    ]
