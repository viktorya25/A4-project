from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        ('Дополнительная информация', {
            'fields': ('avatar',),
        }),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Дополнительная информация', {
            'fields': ('avatar',),
        }),
    )
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff']

admin.site.register(CustomUser, CustomUserAdmin)
