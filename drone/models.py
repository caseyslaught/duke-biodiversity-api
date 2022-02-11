from django.db import models
import uuid

from RainforestApi.common import get_utc_datetime_now


class DroneObservation(models.Model):

    datetime_created = models.DateTimeField(default=get_utc_datetime_now)
    datetime_updated = models.DateTimeField(null=True)
    uid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4)

    photo_s3_object_key = models.CharField(max_length=250, blank=True, null=True)

    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    heading = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    altitude = models.IntegerField(null=True) # meters?
    description = models.TextField(blank=True, null=True)

    # TODO: key to species or drone-vehicle

    class Meta:
        ordering = ['datetime_created']


