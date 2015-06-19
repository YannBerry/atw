# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Initiative',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('project_name', models.CharField(verbose_name='Project Name', max_length=50)),
                ('project_leader', models.CharField(verbose_name='Project Leader', max_length=50)),
                ('picture', models.ImageField(null=True, upload_to='picture/%Y/%m', blank=True)),
                ('description', models.TextField(blank=True)),
                ('nbr_installations', models.IntegerField(verbose_name='Number of Installations', null=True, blank=True)),
                ('power', models.IntegerField(verbose_name='Total Power (kW)', null=True, blank=True)),
                ('start', models.DateField(verbose_name='Beginning of the project', auto_now_add=True)),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
            options={
                'verbose_name_plural': 'Initiatives de projets méthanisation',
            },
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('stage', models.CharField(max_length=25)),
            ],
            options={
                'ordering': ['stage'],
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('status', models.CharField(max_length=25)),
            ],
            options={
                'ordering': ['status'],
            },
        ),
        migrations.AddField(
            model_name='initiative',
            name='stage',
            field=models.ForeignKey(to='map.Stage'),
        ),
        migrations.AddField(
            model_name='initiative',
            name='status',
            field=models.ForeignKey(to='map.Status'),
        ),
    ]
