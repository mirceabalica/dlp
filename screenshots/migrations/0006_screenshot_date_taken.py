# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('screenshots', '0005_screenshot_run_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='screenshot',
            name='date_taken',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 17, 12, 41, 37, 143526, tzinfo=utc), verbose_name=b'date taken'),
            preserve_default=False,
        ),
    ]
