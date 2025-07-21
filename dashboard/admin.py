from django.contrib import admin
from .models import Dashboard

# Register your models here.
class DashboardAdmin(admin.ModelAdmin):
    list_display = ('name', 'profile', 'created_at')
    search_fields = ('name', 'profile__user__username')

admin.site.register(Dashboard, DashboardAdmin)
        
