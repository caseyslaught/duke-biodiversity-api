from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
import uuid

from RainforestApi.common import get_utc_datetime_now


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_staff', False)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


class Client(AbstractBaseUser, PermissionsMixin):
    datetime_created = models.DateTimeField(default=get_utc_datetime_now)
    datetime_updated = models.DateTimeField(null=True)
    uid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4)

    email = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    is_superuser = models.BooleanField(default=False) # project-wide superuser
    is_staff = models.BooleanField(default=False) # super user or agent

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    class Meta:
        ordering = ['email']
        verbose_name = 'client'
        verbose_name_plural = 'clients'



class Project(models.Model):
    
    datetime_created = models.DateTimeField(default=get_utc_datetime_now)
    datetime_updated = models.DateTimeField(null=True)
    uid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4)

    name = models.CharField(max_length=200, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    creator = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)

