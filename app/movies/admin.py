from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

from .models import Movie, CustomUser


@admin.register(CustomUser)
class UserAdmin(DefaultUserAdmin):
    pass


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    fields = (
        "title", "genre", "year", "created_at", "updated_at",
    )
    list_display = (
        "title", "genre", "year", "created_at", "updated_at",
    )
    readonly_fields = (
        "created_at", "updated_at"
    )