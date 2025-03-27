from django.contrib import admin
from .models import TenantItem

@admin.register(TenantItem)
class TenantItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name', 'description')
