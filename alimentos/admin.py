from django.contrib import admin

from .models import Alimento


@admin.register(Alimento)
class AlimentoAdmin(admin.ModelAdmin):
    list_display = [
        'nome', 'quantidade', 'porcao',
        'kcal',
        'carboidratos',
        'proteinas',
        'gorduras',
    ]
    list_display_links = 'nome', 'quantidade', 'porcao'
