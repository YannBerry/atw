# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='initiative',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 8, 15, 49, 28, 533526, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
