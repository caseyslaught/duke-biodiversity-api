# Generated by Django 3.2.12 on 2022-02-11 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drone', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='droneobservation',
            name='altitude',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='droneobservation',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='droneobservation',
            name='heading',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
    ]
