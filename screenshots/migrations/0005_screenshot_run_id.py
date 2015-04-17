# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('screenshots', '0004_auto_20150416_1121'),
    ]

    operations = [
        migrations.AddField(
            model_name='screenshot',
            name='run_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
