from django.contrib import admin
from .models import UserProfile


@admin.register(UserProfile)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('user',)
