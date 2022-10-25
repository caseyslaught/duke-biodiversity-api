from django.contrib import admin

from drone.models import DroneFlight, DroneIdentification, DroneMedia, DroneObservation, DroneVehicle


@admin.register(DroneFlight)
class DroneFlightAdmin(admin.ModelAdmin):
    list_display = ['datetime_created', 'uid']
    search_fields = []
    list_filter = []
    ordering = ['-datetime_created']
    readonly_fields = ['datetime_created']
    exclude = ['datetime_updated']


@admin.register(DroneIdentification)
class DroneIdentificationAdmin(admin.ModelAdmin):
    list_display = ['datetime_created', 'uid']
    search_fields = []
    list_filter = []
    ordering = ['-datetime_created']
    readonly_fields = ['datetime_created']
    exclude = ['datetime_updated']


@admin.register(DroneObservation)
class DroneObservationAdmin(admin.ModelAdmin):
    list_display = ['datetime_created', 'uid']
    search_fields = ['description']
    list_filter = []
    ordering = ['-datetime_created']
    readonly_fields = ['datetime_created']
    exclude = ['datetime_updated']


@admin.register(DroneMedia)
class DroneMediaAdmin(admin.ModelAdmin):
    list_display = ['datetime_created', 'uid', 'geometry']
    search_fields = ['description']
    list_filter = []
    ordering = ['-datetime_created']
    readonly_fields = ['datetime_created']
    exclude = ['datetime_updated']


@admin.register(DroneVehicle)
class DroneVehicleAdmin(admin.ModelAdmin):
    list_display = ['datetime_created', 'uid']
    search_fields = ['name']
    list_filter = []
    ordering = ['-datetime_created']
    readonly_fields = ['datetime_created']
    exclude = ['datetime_updated']

