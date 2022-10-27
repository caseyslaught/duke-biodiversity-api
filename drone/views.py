from django.conf import settings
import os
from rest_framework import permissions, status, generics
from rest_framework.response import Response

from drone import serializers
from drone.models import DroneFlight, DroneMedia, DronePhoto, DroneVehicle
from RainforestApi.common.aws import s3


class CreateDroneFlightView(generics.GenericAPIView):

    permission_classes = [permissions.AllowAny] # IsAuthenticated disabled for now
    serializer_class = serializers.CreateDroneFlightSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data
        run_id = data['run_id']
        drone_id = data['drone_id']
        pilot_name = data.get('pilot_name')

        try:
            drone = DroneVehicle.objects.get(drone_id=drone_id)
        except DroneVehicle.DoesNotExist:
            drone = DroneVehicle.objects.create(drone_id=drone_id)

        flight = DroneFlight.objects.create(drone=drone, run_id=run_id, pilot_name=pilot_name)

        return Response({'flight_uid': flight.uid}, status=status.HTTP_201_CREATED)


class CreateDroneMediaView(generics.GenericAPIView):
    """
    Main view for adding media and photos.
    """
    
    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.CreateDroneMediaSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        valid_data = serializer.validated_data
        flight_uid = valid_data['flight_uid']
        medias = valid_data['data']

        try:
            flight = DroneFlight.objects.get(uid=flight_uid)
        except DroneFlight.DoesNotExist:
            return Response({'error': 'flight_not_found'}, status=status.HTTP_400_BAD_REQUEST)

        response = list()
        for media in medias:

            geometry = media['geometry']
            local_path = media['path']
            format = media['format']

            m = DroneMedia.objects.create(
                flight=flight,
                local_path=local_path,
                file_type=format,
                geometry=geometry)

            response.append({local_path: m.uid})

        return Response(response, status=status.HTTP_201_CREATED)


class CreateDronePhotoView(generics.GenericAPIView):
    """
    Deprecated view for adding photos.
    """

    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.CreateDronePhotoSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data

        flight_uid = data.pop('flight_uid')
        photo_data = data.pop('photo')

        try:
            flight = DroneFlight.objects.get(uid=flight_uid)
        except DroneFlight.DoesNotExist:
            return Response({'error': 'flight_not_found'}, status=status.HTTP_400_BAD_REQUEST)

        o_root, o_ext = os.path.splitext(photo_data.name)
        o_ext = o_ext.lower()
        if o_ext not in ['.jpg', '.jpeg', '.png']:
            return Response({
                'error': 'unsupported_image_file_extension',
                'detail': 'image file extensions supported: .jpg, .jpeg, .png'
            }, status=status.HTTP_400_BAD_REQUEST)

        photo = DronePhoto.objects.create(flight=flight, **data)

        s3_object_key = f'{settings.S3_DATA_PREFIX}/drone/{flight.uid}/{photo.uid}{o_ext}'

        photo.flight = flight
        photo.s3_object_key=s3_object_key
        photo.save()

        photo_data.file.seek(0)
        s3.put_s3_item(
            body=photo_data.file.read(),
            bucket=settings.AWS_S3_DATA_BUCKET,
            object_key=s3_object_key)

        return Response(status=status.HTTP_201_CREATED)


class GetDroneFlightsView(generics.ListAPIView):
    
    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.GetDroneFlightsSerializer

    def get_queryset(self):
        return DroneFlight.objects.all()



