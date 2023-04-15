from django.contrib import admin
from django.contrib.auth import admin as auth_admin

from .models import User


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    model = User
    list_display = 'first_name', 'last_name', 'email'
    list_display_links = 'first_name', 'last_name', 'email'
    fieldsets = auth_admin.UserAdmin.fieldsets + (
        ("Informações do Usuário", {"fields": (
            "telefone",
        )}),
    )
