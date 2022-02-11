from django.conf import settings
from rest_framework import permissions, status, generics
from rest_framework.response import Response
import os

from drone import serializers
from drone.models import DroneObservation
from RainforestApi.common.aws import s3


class AddObservationView(generics.GenericAPIView):

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.AddObservationSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data

        photo = data.pop('photo')

        o_root, o_ext = os.path.splitext(photo.name)
        o_ext = o_ext.lower()
        if o_ext not in ['.jpg', '.jpeg', '.png']:
            return Response({
                'error': 'unsupported_image_file_extension',
                'detail': 'image file extensions supported: .jpg, .jpeg, .png'
            }, status=status.HTTP_400_BAD_REQUEST)

        observation = DroneObservation.objects.create(**data)

        photo_s3_object_key = f'{settings.S3_DATA_PREFIX}/drone/{observation.uid}{o_ext}'

        observation.photo_s3_object_key=photo_s3_object_key
        observation.save()

        photo.file.seek(0)
        s3.put_s3_item(
            body=photo.file.read(),
            bucket=settings.AWS_S3_DATA_BUCKET,
            object_key=photo_s3_object_key,
        )

        return Response(status=status.HTTP_201_CREATED)


class GetObservationsView(generics.ListAPIView):

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.GetObservationsSerializer

    def get_queryset(self):
        return DroneObservation.objects.all()
    
