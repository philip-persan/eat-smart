from django.contrib import admin

from .models import UserPerfil


@admin.register(UserPerfil)
class UserPefilAdmin(admin.ModelAdmin):
    list_display = [
        'user', 'idade', 'genero', 'altura',
        'peso_atual', 'peso_alvo', 'nivel_de_atividade',
        'GEAF', 'GET'
    ]
    list_display_links = 'user', 'genero', 'altura'
