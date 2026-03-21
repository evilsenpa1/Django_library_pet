
from django.contrib import admin
from .models import AuthorModel


@admin.register(AuthorModel)
class AuthorModelAdmin(admin.ModelAdmin):
    pass
