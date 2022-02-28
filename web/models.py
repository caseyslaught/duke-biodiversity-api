from django.db import models
import uuid

from RainforestApi.common import get_utc_datetime_now


class Species(models.Model):

    datetime_created = models.DateTimeField(default=get_utc_datetime_now)
    datetime_updated = models.DateTimeField(null=True)
    uid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4)

    latin_name = models.CharField(max_length=200, blank=True, null=True)
    common_name = models.CharField(max_length=200, blank=True, null=True)

    kingdom = models.CharField(max_length=100, blank=True, null=True)
    phylum = models.CharField(max_length=100, blank=True, null=True)

