from django.contrib import admin

from account.models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['email', 'name']
    search_fields = ['email', 'name']
    list_filter = []
    ordering = ['email']
    readonly_fields = ['datetime_created']
    exclude = ['datetime_updated']

