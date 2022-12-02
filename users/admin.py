from django.contrib import admin
from .models import CustomUser, CustomUserProfile
from django.contrib.auth.admin import UserAdmin

# Register your models here.


class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'company_name', 'username', 'role', 'is_active')
    ordering = ('-date_joined',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(CustomUserProfile)