# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-10 12:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0043_auto_20160610_1234'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=30, verbose_name='Pays')),
            ],
            options={
                'ordering': ['country'],
                'verbose_name': 'Pays',
                'verbose_name_plural': 'Pays',
            },
        ),
    ]
