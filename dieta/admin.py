from django.contrib import admin

from .models import Dieta


@admin.register(Dieta)
class DietaAdmin(admin.ModelAdmin):
    list_display = [
        'user', 'macros', 'qtd_refeicoes', 'kcal_total',
        'carbo_total', 'carbo_por_refeicao',
        'proteina_total', 'proteina_por_refeicao',
        'gordura_total', 'gordura_por_refeicao',
    ]
    list_display_links = 'user', 'macros'
