# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('screenshots', '0002_auto_20150409_0643'),
    ]

    operations = [
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('domain', models.CharField(default=b'', max_length=512)),
            ],
        ),
        migrations.AlterField(
            model_name='screenshot',
            name='domain',
            field=models.ForeignKey(to='screenshots.Domain'),
        ),
    ]
