from django.contrib import admin

# Register your models here.
from apps.clients.models import Clients


@admin.register(Clients)
class ClientsProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'fullname')
    search_fields = ('id', 'fullname')
