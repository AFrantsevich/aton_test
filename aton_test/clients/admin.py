from django.contrib import admin
from .models import Client


class UserInline(admin.TabularInline):
    model = Client.response_person.through


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    inlines = [
        UserInline,
    ]
    list_display = 'bank_account_number', 'status'
