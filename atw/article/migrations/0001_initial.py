# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-02 08:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25, verbose_name='Article')),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['title'],
                'verbose_name_plural': 'Articles',
                'verbose_name': 'Article',
            },
        ),
    ]