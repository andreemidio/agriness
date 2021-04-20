from django.contrib import admin

# Register your models here.
from apps.books.models import Books


@admin.register(Books)
class BooksProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('id', 'title')