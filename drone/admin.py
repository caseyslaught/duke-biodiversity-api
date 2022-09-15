from django.contrib import admin

from drone.models import DroneFlight, DroneObservation


@admin.register(DroneFlight)
class DroneFlightAdmin(admin.ModelAdmin):
    list_display = ['datetime_created']
    search_fields = []
    list_filter = []
    ordering = ['-datetime_created']
    readonly_fields = ['datetime_created']
    exclude = ['datetime_updated']


@admin.register(DroneObservation)
class DroneObservationAdmin(admin.ModelAdmin):
    list_display = ['datetime_created', 'latitude', 'longitude', 'description']
    search_fields = ['description']
    list_filter = []
    ordering = ['-datetime_created']
    readonly_fields = ['datetime_created']
    exclude = ['datetime_updated']

