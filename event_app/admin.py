from django.contrib import admin
from event_app.models import Organization, Event
from django.utils.safestring import mark_safe


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("title", "address", "postcode")
    list_filter = ("title", )
    search_fields = ("title__startswith", )


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "preview")
    list_filter = ("title", "date", )
    search_fields = ("title__startswith", "date__startswith",)

    readonly_fields = ["preview"]

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="max-height: 150px;">')

