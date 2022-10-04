from rest_framework import serializers

from drone.models import DroneFlight, DroneObservation, DronePhoto, DroneVehicle


class CreateDroneFlightSerializer(serializers.Serializer):

    drone_id = serializers.CharField()
    pilot_name = serializers.CharField()
    # log_file = serializers.FileField(allow_empty_file=False, allow_null=True)

    class Meta:
        ref_name = 'DroneAddFlightSerializer'


class CreateDronePhotoSerializer(serializers.ModelSerializer):
    
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


class GetDroneVehicleSerializer(serializers.ModelSerializer):

    class Meta:
        model = DroneVehicle
        fields = [
            "uid",
            "name",
            "drone_id"
        ]


class GetDroneFlightsSerializer(serializers.ModelSerializer):

    drone = GetDroneVehicleSerializer()

    class Meta:
        model = DroneFlight
        fields = [
            'uid', 
            'datetime_created', 
            'pilot_name', 
            'flight_path',
            'drone'
        ]


class GetDronePhotosSerializer(serializers.ModelSerializer):

    # TODO: move base url to settings
    photo_href = serializers.SerializerMethodField() 
    def get_photo_href(self, obj):
        return f'https://d2dr0xu4tpg6v2.cloudfront.net/{obj.photo_s3_object_key}'

    class Meta:
        model = DronePhoto
        exclude = ['id', 'photo_s3_object_key']



