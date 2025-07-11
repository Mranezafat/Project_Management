from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'email', 'date_joined', 'avatar', 'bio')
    search_fields = ('user__username', 'email')
    list_filter = ('date_joined',)


admin.site.register(Profile, ProfileAdmin)
# Register your models here.
