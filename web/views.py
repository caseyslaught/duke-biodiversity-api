from unicodedata import category
from django.conf import settings
from django.db.models import Q
from rest_framework import permissions, status, generics
from rest_framework.response import Response
import os

from camera_trap.models import CameraTrapObservation
from camera_trap.serializers import GetObservationsSerializer as GetCameraTrapObsSerializer
from drone.models import DroneObservation
from drone.serializers import GetObservationsSerializer as GetDroneObsSerializer
from web import serializers


class GetObservationsView(generics.GenericAPIView):

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.GetObservationsSerializer


    def get(self, request):
        serializer = serializers.GetObservationsFiltersSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        filters = serializer.data

        categories = [c for c in filters['categories'].split(',') if c != '']
        methods = [m for m in filters['methods'].split(',') if m != '']
        levels = [l for l in filters['levels'].split(',') if l != '']

        data = dict()

        if 'Acoustic' in methods:
            data['Acoustic'] = []

        if 'Camera trap' in methods:
            camera_obs = CameraTrapObservation.objects.filter(
                Q(category__in=categories) | Q(category='') | Q(category__isnull=True),
                Q(level__in=levels) | Q(level='') | Q(level__isnull=True)
            )
            camera_ser = GetCameraTrapObsSerializer(camera_obs, many=True)
            data['Camera trap'] = camera_ser.data

        if 'DNA' in methods:
            data['DNA'] = []

        if 'Drone' in methods:
            drone_obs = DroneObservation.objects.filter(
                Q(category__in=categories) | Q(category='') | Q(category__isnull=True),
                Q(level__in=levels) | Q(level='') | Q(level__isnull=True)
            ).all()
            drone_ser = GetDroneObsSerializer(drone_obs, many=True)
            data['Drone'] = drone_ser.data


        return Response(data, status=status.HTTP_200_OK)

