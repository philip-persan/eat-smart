from django.contrib import admin

from .models import MetaMacro


@admin.register(MetaMacro)
class MetaMacroAdmin(admin.ModelAdmin):
    list_display = 'user', 'descricao', 'carboidratos', 'proteinas', 'gorduras'
    list_display_links = 'user', 'descricao', 'carboidratos', 'proteinas', 'gorduras'  # noqa
