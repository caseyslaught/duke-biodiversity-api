from django.contrib import admin

from camera_trap.models import CameraTrapObservation


@admin.register(CameraTrapObservation)
class CameraTrapObservationAdmin(admin.ModelAdmin):
    list_display = ['datetime_created', 'latitude', 'longitude', 'description']
    search_fields = ['description']
    list_filter = []
    ordering = ['-datetime_created']
    readonly_fields = ['datetime_created']
    exclude = ['datetime_updated']

