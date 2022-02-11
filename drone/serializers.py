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
            'description',
            'photo',
        ]


class GetObservationsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = DroneObservation
        fields = '__all__'

