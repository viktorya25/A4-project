from django.contrib import admin

from services.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'service',
        'status',
        'completion_date',
        'is_completed',
    )
    list_filter = ('status', 'is_completed')
    search_fields = ('id', 'user__username', 'service')
    readonly_fields = ('id', 'user', 'service', 'created_at',)
    fields = (
        'id',
        'user',
        'service',
        'created_at',
        'description',
        'price',
        'status',
        'completion_date',
        'is_completed',
    )