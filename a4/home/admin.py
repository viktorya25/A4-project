from django.contrib import admin

from home.models import Application


@admin.register(Application)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'email',
        'created_at',
    )
    search_fields = (
        'id',
        'name',
        'email',
        'created_at',
    )