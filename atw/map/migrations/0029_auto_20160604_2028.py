# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-04 18:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0028_remove_trip_trip_stages'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tripstagetrip',
            name='trip',
        ),
        migrations.RemoveField(
            model_name='tripstagetrip',
            name='tripstage',
        ),
        migrations.DeleteModel(
            name='TripStageTrip',
        ),
    ]
