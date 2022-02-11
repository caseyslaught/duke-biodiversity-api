from django.contrib import admin

from drone.models import DroneObservation


@admin.register(DroneObservation)
class DroneObservationAdmin(admin.ModelAdmin):
    list_display = ['datetime_created', 'latitude', 'longitude', 'description']
    search_fields = ['description']
    list_filter = []
    ordering = ['-datetime_created']
    readonly_fields = ['datetime_created']
    exclude = ['datetime_updated']

