# Generated by Django 3.2.12 on 2022-03-24 15:19

import RainforestApi.common
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('drone', '0004_auto_20220217_1831'),
    ]

    operations = [
        migrations.CreateModel(
            name='DroneFlight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_created', models.DateTimeField(default=RainforestApi.common.get_utc_datetime_now)),
                ('datetime_updated', models.DateTimeField(null=True)),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('geojson', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='droneobservation',
            name='flight',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='drone.droneflight'),
        ),
    ]