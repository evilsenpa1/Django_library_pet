
from django.contrib import admin
from .models import AuthorModel


@admin.register(AuthorModel)
class AuthorModelAdmin(admin.ModelAdmin):
    list_display = ["name", "date_of_birth", "pub_date"]
    search_fields = ["name"]
    filter_horizontal = ["books"]
