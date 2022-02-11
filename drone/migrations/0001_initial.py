# Generated by Django 3.2.12 on 2022-02-11 18:58

import RainforestApi.common
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DroneObservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_created', models.DateTimeField(default=RainforestApi.common.get_utc_datetime_now)),
                ('datetime_updated', models.DateTimeField(null=True)),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('photo_s3_object_key', models.CharField(blank=True, max_length=250, null=True)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('heading', models.DecimalField(decimal_places=2, max_digits=5)),
                ('altitude', models.IntegerField()),
                ('description', models.TextField()),
            ],
            options={
                'ordering': ['datetime_created'],
            },
        ),
    ]
