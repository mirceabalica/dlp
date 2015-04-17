# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
        ('screenshots', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='screenshot',
            name='production_image',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(location=b'/home/mircea/Work/djangoapp/bentoqa/screenshots/images'), max_length=256, null=True, upload_to=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='screenshot',
            name='qa_image',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(location=b'/home/mircea/Work/djangoapp/bentoqa/screenshots/images'), max_length=256, null=True, upload_to=b'', blank=True),
        ),
    ]
