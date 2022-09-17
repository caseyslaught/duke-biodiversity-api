from django.conf import settings
import json
import os
from rest_framework import permissions, status, generics
from rest_framework.response import Response

from drone import serializers
from drone.models import DroneFlight, DroneObservation, DroneVehicle
from RainforestApi.common.aws import s3


class CreateFlightView(generics.GenericAPIView):

    permission_classes = [permissions.AllowAny] # IsAuthenticated disabled for now
    serializer_class = serializers.CreateFlightSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data
        drone_id = data['drone_id']
        pilot_name = data['pilot_name']
        log_file = data['log_file']

        try:
            drone = DroneVehicle.objects.get(drone_id=drone_id)
        except DroneVehicle.DoesNotExist:
            drone = DroneVehicle.objects.create(drone_id=drone_id)

        flight = DroneFlight.objects.create(drone=drone, pilot_name=pilot_name) # TODO: add flight_path

        return Response({'flight_uid': flight.uid}, status=status.HTTP_201_CREATED)


class CreateObservationView(generics.GenericAPIView):

    permission_classes = [permissions.AllowAny] # IsAuthenticated disabled for now
    serializer_class = serializers.CreateObservationSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data

        flight_uid = data.pop('flight_uid')
        photo = data.pop('photo')

        try:
            flight = DroneFlight.objects.get(uid=flight_uid)
        except DroneFlight.DoesNotExist:
            return Response({'error': 'flight_not_found'}, status=status.HTTP_400_BAD_REQUEST)

        o_root, o_ext = os.path.splitext(photo.name)
        o_ext = o_ext.lower()
        if o_ext not in ['.jpg', '.jpeg', '.png']:
            return Response({
                'error': 'unsupported_image_file_extension',
                'detail': 'image file extensions supported: .jpg, .jpeg, .png'
            }, status=status.HTTP_400_BAD_REQUEST)

        # TODO: get lat/lon/alt from photo exif data
        observation = DroneObservation.objects.create(**data)

        photo_s3_object_key = f'{settings.S3_DATA_PREFIX}/drone/{observation.uid}{o_ext}'

        observation.flight = flight
        observation.photo_s3_object_key=photo_s3_object_key
        observation.save()

        photo.file.seek(0)
        s3.put_s3_item(
            body=photo.file.read(),
            bucket=settings.AWS_S3_DATA_BUCKET,
            object_key=photo_s3_object_key)

        return Response(status=status.HTTP_201_CREATED)


class GetFlightsView(generics.ListAPIView):
    
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.GetFlightsSerializer

    def get_queryset(self):
        return DroneFlight.objects.all()


class GetObservationsView(generics.ListAPIView):

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.GetObservationsSerializer

    # TODO: add filter for specific flight

    def get_queryset(self):
        return DroneObservation.objects.all()
    
