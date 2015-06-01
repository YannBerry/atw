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
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('project_name', models.CharField(verbose_name='Project Name', max_length=50)),
                ('status', models.CharField(max_length=50)),
                ('stage', models.CharField(max_length=50)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='picture/%Y/%m')),
                ('description', models.TextField(blank=True)),
                ('project_leader', models.CharField(verbose_name='Project Leader', max_length=50)),
                ('nbr_installations', models.IntegerField(blank=True, null=True, verbose_name='Number of Installations')),
                ('power', models.IntegerField(blank=True, null=True, verbose_name='Total Power (kW)')),
                ('start', models.DateField(auto_now_add=True, verbose_name='Beginning of the project')),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
            options={
                'verbose_name_plural': 'Initiatives de projets méthanisation',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('stage', models.CharField(max_length=25)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('status', models.CharField(max_length=25)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
