from django.contrib import admin

from drone.models import DroneFlight, DroneIdentification, DroneObservation, DronePhoto, DroneVehicle


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


@admin.register(DronePhoto)
class DronePhotoAdmin(admin.ModelAdmin):
    list_display = ['datetime_created', 'uid']
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

