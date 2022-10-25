from importlib.resources import path
from rest_framework import serializers

from drone.models import DroneFlight, DroneMedia, DroneObservation, DronePhoto, DroneVehicle


### CREATE

class CreateDroneFlightSerializer(serializers.Serializer):

    drone_id = serializers.CharField()
    pilot_name = serializers.CharField(allow_blank=True, allow_null=True)

    class Meta:
        ref_name = 'DroneAddFlightSerializer'


# Geo-field...


class CreateMediaSerializer(serializers.Serializer):
    """
    Sub-serializer for creating a single media.
    """
    
    # lat = serializers.DecimalField(max_digits=12, decimal_places=6)
    # lng = serializers.DecimalField(max_digits=12, decimal_places=6)
    # alt = serializers.DecimalField(max_digits=10, decimal_places=2)
    geometry = serializers.CharField() # geojson

    path = serializers.CharField()
    format = serializers.CharField() # jpg, png, mp4
    datetime_recorded = serializers.DateTimeField()


class CreateDroneMediaSerializer(serializers.Serializer):
    """
    Main serializer for creating many medias.
    """

    flight_uid = serializers.UUIDField()
    data = CreateMediaSerializer(many=True)


### GET

class GetDroneVehicleSerializer(serializers.ModelSerializer):
    """
    Main serializer for getting drone vehicles.
    """

    class Meta:
        model = DroneVehicle
        fields = [
            "uid",
            "name",
            "drone_id"
        ]


class GetMediaSerializer(serializers.ModelSerializer):
    """
    Main serializer for getting media.
    """

    class Meta:
        model = DroneMedia
        fields = [
            'uid',
            'datetime_recorded',
            'latitude',
            'longitude',
            'altitude',
            'local_path',
            'file_type'
        ]


class GetDroneFlightsSerializer(serializers.ModelSerializer):
    """
    Main serializer for getting a drone flight info including media.
    """

    drone = GetDroneVehicleSerializer()
    medias = GetMediaSerializer(many=True)

    class Meta:
        model = DroneFlight
        fields = [
            'uid', 
            'datetime_created', 
            'pilot_name', 
            'flight_path',
            'drone',
            'medias'
        ]


class GetDroneObservationsSerializer(serializers.ModelSerializer):

    flight = GetDroneFlightsSerializer()
    medias = GetMediaSerializer(many=True) # related field

    class Meta:
        model = DroneObservation
        fields = [
            'uid',
            'datetime_created',
            'flight',
            'medias'
        ]







### DEPRECATED


class CreateDronePhotoSerializer(serializers.ModelSerializer):
    """
    Deprecated.
    """
    
    flight_uid = serializers.UUIDField()
    photo = serializers.ImageField(allow_empty_file=False)

    class Meta:
        model = DronePhoto
        fields = [
            'latitude',
            'longitude',
            'altitude',
            'flight_uid',
            'photo',
        ]


class GetDronePhotosSerializer(serializers.ModelSerializer):
    """
    Deprecated.
    """

    # TODO: move base url to settings
    photo_href = serializers.SerializerMethodField() 
    def get_photo_href(self, obj):
        return f'https://d2dr0xu4tpg6v2.cloudfront.net/{obj.photo_s3_object_key}'

    class Meta:
        model = DronePhoto
        exclude = ['id', 'photo_s3_object_key']
