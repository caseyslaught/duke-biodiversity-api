from django.core.management.base import BaseCommand

from camera_trap.models import CameraTrapObservation
from drone.models import DroneObservation


class Command(BaseCommand):
    help = 'Initializes dummy data.'

    def handle(self, *args, **options):
        CameraTrapObservation.objects.all().delete()
        DroneObservation.objects.all().delete()

