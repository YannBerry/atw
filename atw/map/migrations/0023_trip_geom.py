# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-04 08:19
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0022_auto_20160604_0923'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='geom',
            field=django.contrib.gis.db.models.fields.PointField(default='POINT(0.0 0.0)', srid=4326),
        ),
    ]
