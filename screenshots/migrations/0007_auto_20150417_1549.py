# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('screenshots', '0006_screenshot_date_taken'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='screenshot',
            name='date_taken',
        ),
        migrations.AddField(
            model_name='screenshot',
            name='production_date_taken',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 17, 12, 48, 44, 724943, tzinfo=utc), verbose_name=b'production_date taken'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='screenshot',
            name='qa_date_taken',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 17, 12, 49, 1, 820280, tzinfo=utc), verbose_name=b'qa_date taken'),
            preserve_default=False,
        ),
    ]
