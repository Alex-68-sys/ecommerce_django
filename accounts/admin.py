from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
       model = CustomUser
       fieldsets = UserAdmin.fieldsets + (
        ('Extra Info', {
            'fields': ('address', 'is_store_manager'),
        }),
    ) 

admin.site.register(CustomUser, CustomUserAdmin)