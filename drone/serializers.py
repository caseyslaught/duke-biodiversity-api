from rest_framework import serializers

from drone.models import DroneObservation


class AddObservationSerializer(serializers.ModelSerializer):
    
    photo = serializers.ImageField(allow_empty_file=False)

    class Meta:
        model = DroneObservation
        fields = [
            'latitude',
            'longitude',
            'heading',
            'altitude',
            'altitude_above_ground',
            'description',
            'photo',
        ]


class GetObservationsSerializer(serializers.ModelSerializer):
    
    photo_href = serializers.SerializerMethodField() 
    def get_photo_href(self, obj):
        return f'https://d2dr0xu4tpg6v2.cloudfront.net/{obj.photo_s3_object_key}'

    method = serializers.SerializerMethodField()
    def get_method(self, obj):
        return "Drone"

    class Meta:
        model = DroneObservation
        #fields = '__all__'
        exclude = ['id', 'photo_s3_object_key']

