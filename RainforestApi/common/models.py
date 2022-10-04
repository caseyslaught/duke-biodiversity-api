from django.db import models
import uuid

from camera_trap.models import CameraTrapObservation
from drone.models import DroneObservation
from RainforestApi.common import get_utc_datetime_now


