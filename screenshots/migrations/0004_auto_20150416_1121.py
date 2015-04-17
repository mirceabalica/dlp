# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('screenshots', '0003_auto_20150416_0728'),
    ]

    operations = [
        migrations.RenameField(
            model_name='domain',
            old_name='domain',
            new_name='url',
        ),
    ]
