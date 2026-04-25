from django.contrib import admin
from .models import BookModel


@admin.register(BookModel)
class BookModelAdmin(admin.ModelAdmin):
    list_display = ["name", "date", "pub_date"]
    search_fields = ["name", "description"]
