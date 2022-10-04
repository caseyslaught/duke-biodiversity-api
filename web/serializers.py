from rest_framework import serializers


class GetObservationsFiltersSerializer(serializers.Serializer):
    categories = serializers.CharField(allow_blank=True)
    levels = serializers.CharField(allow_blank=True)
    methods = serializers.CharField(allow_blank=True)


class GetObservationsSerializer(serializers.Serializer):
    pass
