# Generated by Django 4.2 on 2023-04-16 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('alimentos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Refeicao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=70, null=True, verbose_name='Descrição')),
                ('alimentos', models.ManyToManyField(to='alimentos.alimento', verbose_name='Alimentos')),
            ],
            options={
                'verbose_name': 'Refeição',
                'verbose_name_plural': 'Refeições',
            },
        ),
    ]
