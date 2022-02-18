from rest_framework import serializers

from drone.models import DroneObservation
from drone.serializers import GetObservationsSerializer


class GetObservationsFiltersSerializer(serializers.Serializer):
    categories = serializers.CharField(allow_blank=True)
    levels = serializers.CharField(allow_blank=True)
    methods = serializers.CharField(allow_blank=True)


class GetObservationsSerializer(serializers.Serializer):
    pass
