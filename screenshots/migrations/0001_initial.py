# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Screenshot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('domain', models.CharField(default=b'', max_length=512)),
                ('qa_image', models.CharField(default=b'', max_length=256)),
                ('production_image', models.CharField(default=b'', max_length=256)),
            ],
        ),
    ]
