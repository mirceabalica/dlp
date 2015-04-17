# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('screenshots', '0007_auto_20150417_1549'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='screenshot',
            name='production_date_taken',
        ),
        migrations.RemoveField(
            model_name='screenshot',
            name='qa_date_taken',
        ),
        migrations.AddField(
            model_name='screenshot',
            name='date_taken',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 17, 12, 53, 9, 261548, tzinfo=utc), verbose_name=b'date taken'),
            preserve_default=False,
        ),
    ]
