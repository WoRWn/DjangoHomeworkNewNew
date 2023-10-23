from .models import Advertisment
from django.contrib import admin


class AdvertismentAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'updated_date', 'created_date', 'action']
    list_filter = ['action', 'created_at']
    actions = ["make_action_as_false", "make_action_as_true"]
    fieldsets = (
        ('Общее', {
            'fields': ('title', 'description')
        }),
        ('Финансы', {
            'fields': ('price', 'action'),
            'classes': ['collapse']
        })
    )

    @admin.action(description="Убрать возможность торга")
    def make_action_as_false(self, request, queryset):
        queryset.update(action=False)

    @admin.action(description="Добавить возможность торга")
    def make_action_as_true(self, request, queryset):
        queryset.update(action=True)


admin.site.register(Advertisment, AdvertismentAdmin)

