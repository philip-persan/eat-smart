from django.contrib import admin

from .models import Refeicao


@admin.register(Refeicao)
class RefeicaoAdmin(admin.ModelAdmin):
    list_display = [
        'descricao', 'total_kcal',
        'total_carboidratos', 'total_proteinas',
        'total_gorduras'
    ]
    list_display_links = 'descricao',
