from django.db import models
import uuid

from RainforestApi.common import get_utc_datetime_now


class DroneVehicle(models.Model):

    datetime_created = models.DateTimeField(default=get_utc_datetime_now)
    datetime_updated = models.DateTimeField(null=True)
    uid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4)

    name = models.CharField(max_length=100, blank=True, null=True)
    drone_id = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.drone_id} - {self.name}'


class DroneFlight(models.Model):

    datetime_created = models.DateTimeField(default=get_utc_datetime_now)
    datetime_updated = models.DateTimeField(null=True)
    uid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4)

    drone = models.ForeignKey(DroneVehicle, on_delete=models.CASCADE, null=True)
    pilot_name = models.CharField(max_length=100, blank=True, null=True)
    flight_path = models.TextField(blank=True, null=True) # geojson LineString

    def __str__(self) -> str:
        return f'{self.uid} - {self.pilot_name}'


class DroneObservation(models.Model):

    datetime_created = models.DateTimeField(default=get_utc_datetime_now)
    datetime_updated = models.DateTimeField(null=True)
    uid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4)

    flight = models.ForeignKey(DroneFlight, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['datetime_created']


class DronePhoto(models.Model):

    datetime_created = models.DateTimeField(default=get_utc_datetime_now)
    datetime_updated = models.DateTimeField(null=True)
    uid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4)

    s3_object_key = models.CharField(max_length=250, blank=True, null=True)

    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    altitude = models.IntegerField(null=True) # meters

    flight = models.ForeignKey(DroneFlight, on_delete=models.CASCADE, related_name='photos')
    observation = models.ForeignKey(DroneObservation, on_delete=models.CASCADE, null=True, related_name='photos')


class DroneIdentification(models.Model):

    datetime_created = models.DateTimeField(default=get_utc_datetime_now)
    datetime_updated = models.DateTimeField(null=True)
    uid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4)

    common_name = models.CharField(max_length=200)
    latin_name = models.CharField(max_length=200)

    # iNaturalist stuff, source (i.e. manual, iNat, etc.)

    observation = models.ForeignKey(DroneObservation, on_delete=models.CASCADE, related_name='identifications')

