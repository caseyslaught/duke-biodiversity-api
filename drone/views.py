from django.conf import settings
import json
import os
from rest_framework import permissions, status, generics
from rest_framework.response import Response

from drone import serializers
from drone.models import DroneFlight, DroneObservation
from RainforestApi.common.aws import s3


class AddFlightView(generics.GenericAPIView):

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.AddFlightSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data
        geojson = data.get('geojson')

        flight = DroneFlight.objects.create()

        if geojson:
            geojson = json.loads(geojson)
            print(geojson)
            features = geojson['features']
            if len(features) > 1:
                flight.delete()
                return Response({
                    'error': 'maximum_one_feature',
                    'detail': 'You can only add one feature.'
                }, status=status.HTTP_400_BAD_REQUEST)

            if features[0]['geometry']['type'] != "LineString":
                flight.delete()
                return Response({
                    'error': 'linestring_required',
                    'detail': 'The feature must be a LineString.'
                }, status=status.HTTP_400_BAD_REQUEST)

            flight.geojson = data['geojson']
            flight.save()

        return Response({'flight_uid': flight.uid}, status=status.HTTP_201_CREATED)


class AddObservationView(generics.GenericAPIView):

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.AddObservationSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data

        flight_uid = data.pop('flight_uid')
        photo = data.pop('photo')

        try:
            flight = DroneFlight.get(uid=flight_uid)
        except DroneFlight.DoesNotExist:
            flight = DroneFlight.objects.create()

        o_root, o_ext = os.path.splitext(photo.name)
        o_ext = o_ext.lower()
        if o_ext not in ['.jpg', '.jpeg', '.png']:
            return Response({
                'error': 'unsupported_image_file_extension',
                'detail': 'image file extensions supported: .jpg, .jpeg, .png'
            }, status=status.HTTP_400_BAD_REQUEST)

        observation = DroneObservation.objects.create(**data)

        photo_s3_object_key = f'{settings.S3_DATA_PREFIX}/drone/{observation.uid}{o_ext}'

        observation.flight = flight
        observation.photo_s3_object_key=photo_s3_object_key
        observation.save()

        photo.file.seek(0)
        s3.put_s3_item(
            body=photo.file.read(),
            bucket=settings.AWS_S3_DATA_BUCKET,
            object_key=photo_s3_object_key,
        )

        return Response(status=status.HTTP_201_CREATED)


class GetFlightsView(generics.ListAPIView):
    
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.GetFlightsSerializer

    def get_queryset(self):
        return DroneFlight.objects.all()


class GetObservationsView(generics.ListAPIView):

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.GetObservationsSerializer

    def get_queryset(self):
        return DroneObservation.objects.all()
    
