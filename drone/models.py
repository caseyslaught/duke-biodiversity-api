from django.db import models
import uuid

from RainforestApi.common import get_utc_datetime_now


class DroneFlight(models.Model):

    datetime_created = models.DateTimeField(default=get_utc_datetime_now)
    datetime_updated = models.DateTimeField(null=True)
    uid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4)

    geojson = models.TextField(blank=True, null=True) # LineString


class DroneObservation(models.Model):

    datetime_created = models.DateTimeField(default=get_utc_datetime_now)
    datetime_updated = models.DateTimeField(null=True)
    uid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4)

    photo_s3_object_key = models.CharField(max_length=250, blank=True, null=True)

    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    heading = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    altitude = models.IntegerField(null=True) # meters?
    altitude_above_ground = models.IntegerField(null=True) # meters?
    description = models.TextField(blank=True, null=True)

    category = models.CharField(max_length=100, blank=True, null=True) # Birds, Mammals, Plants
    level = models.CharField(max_length=100, blank=True, null=True) # Floor, Understory, Canopy

    flight = models.ForeignKey(DroneFlight, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['datetime_created']



