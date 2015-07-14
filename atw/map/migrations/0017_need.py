# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0016_auto_20150714_1906'),
    ]

    operations = [
        migrations.CreateModel(
            name='Need',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('need', models.CharField(verbose_name='Need', max_length=25)),
            ],
            options={
                'verbose_name': 'Need',
                'verbose_name_plural': 'Needs',
                'ordering': ['need'],
            },
        ),
    ]
