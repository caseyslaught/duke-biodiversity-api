from datetime import datetime, timedelta, timezone
from django.core.management.base import BaseCommand
from random import randrange, uniform

from camera_trap.models import CameraTrapObservation
from drone.models import DroneObservation

class Command(BaseCommand):
    help = 'Initializes dummy data.'

    def handle(self, *args, **options):
        categories = ["Birds", "Insects", "Mammals", "Plants"]
        levels = ["Floor", "Understory", "Canopy", "Emergent"]

        lats = [36.012530, 36.022197]
        lngs = [ -78.937774, -78.915939]

        images = [
            "testing/c1.jpg",
            "testing/c2.jpg",
            "testing/c3.jpg",
            "testing/c4.jpg",
        ]

        for cat in categories:
            for lev in levels:
                for i in range(2):
                    CameraTrapObservation.objects.create(
                        latitude=uniform(lats[0], lats[1]),
                        longitude=uniform(lngs[0], lngs[1]),
                        heading=randrange(0, 360),
                        altitude=randrange(0, 200),
                        altitude_above_ground=randrange(0, 20),
                        description="",
                        category=cat,
                        level=lev,
                        photo_s3_object_key=images[randrange(0, 3)]
                    )
                    DroneObservation.objects.create(
                        latitude=uniform(lats[0], lats[1]),
                        longitude=uniform(lngs[0], lngs[1]),
                        heading=randrange(0, 360),
                        altitude=randrange(0, 200),
                        altitude_above_ground=randrange(0, 20),
                        description="",
                        category=cat,
                        level=lev,
                        photo_s3_object_key=images[randrange(0, 3)]
                    )
                        
