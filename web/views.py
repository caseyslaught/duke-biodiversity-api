from django.conf import settings
from django.db.models import Q
from rest_framework import permissions, status, generics
from rest_framework.response import Response
import os

from web import serializers
from drone.models import DroneObservation
from drone.serializers import GetObservationsSerializer as GetDroneObsSerializer


class GetObservationsView(generics.GenericAPIView):

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.GetObservationsSerializer


    def get(self, request):
        serializer = serializers.GetObservationsFiltersSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        filters = serializer.data

        categories = [cat for cat in filters['categories'].split(',') if cat != '']
        methods = [met for met in filters['methods'].split(',') if met != '']
        levels = [lev for lev in filters['levels'].split(',') if lev != '']

        data = dict()

        if 'Acoustic' in methods:
            pass

        if 'Camera trap' in methods:
            pass

        if 'Drone' in methods:
            drone_obs = DroneObservation.objects.filter(
                Q(category__in=categories) | Q(category='') | Q(category__isnull=True),
                Q(level__in=levels) | Q(level='') | Q(level__isnull=True)
            ).all()
            drone_ser = GetDroneObsSerializer(drone_obs, many=True)
            data['drone'] = drone_ser.data


        return Response(data, status=status.HTTP_200_OK)

