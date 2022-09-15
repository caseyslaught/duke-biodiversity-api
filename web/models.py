from django.db import models
import uuid

from RainforestApi.common import get_utc_datetime_now


class Species(models.Model):

    datetime_created = models.DateTimeField(default=get_utc_datetime_now)
    datetime_updated = models.DateTimeField(null=True)
    uid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4)

    scientific_name = models.CharField(max_length=200, blank=True, null=True)
    common_name = models.CharField(max_length=200, blank=True, null=True)

    tax_kingdom = models.CharField(max_length=100, blank=True, null=True)
    tax_phylum = models.CharField(max_length=100, blank=True, null=True)
    tax_class = models.CharField(max_length=100, blank=True, null=True)

    iucn_status = models.CharField(max_length=50, blank=True, null=True)

    # arborial / groundwelling
    # diurnal / nocturnal
    # carnivore / herbivore
    # size (small, medium, large)

