# Generated by Django 4.2 on 2023-04-16 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, null=True, verbose_name='Nome do alimento')),
                ('porcao', models.CharField(choices=[('Unidade', 'Unidade'), ('Gramas', 'Gramas')], max_length=50, null=True, verbose_name='Proção')),
                ('kcal', models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='Kcal')),
                ('carboidratos', models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='Carboidratos')),
                ('proteinas', models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='Proteínas')),
                ('gorduras', models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='Gorduras')),
                ('quantidade', models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='Quantidade')),
            ],
            options={
                'verbose_name': 'Alimento',
                'verbose_name_plural': 'Alimentos',
                'ordering': ('nome',),
            },
        ),
    ]
