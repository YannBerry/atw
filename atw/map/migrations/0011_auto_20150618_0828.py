# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0010_auto_20150618_0001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='initiative',
            name='date_published',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date published'),
        ),
        migrations.AlterField(
            model_name='initiative',
            name='email_validation',
            field=models.BooleanField(verbose_name='Email validation'),
        ),
        migrations.AlterField(
            model_name='initiative',
            name='picture',
            field=models.ImageField(null=True, upload_to='picture/%Y/%m', verbose_name='Picture', blank=True),
        ),
        migrations.AlterField(
            model_name='stage',
            name='stage',
            field=models.CharField(max_length=25, verbose_name='Stage'),
        ),
    ]
