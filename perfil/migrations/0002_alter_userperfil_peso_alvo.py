# Generated by Django 4.2 on 2023-04-15 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userperfil',
            name='peso_alvo',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='Peso alvo'),
        ),
    ]
