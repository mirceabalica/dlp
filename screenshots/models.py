import datetime
import pytz
from django.db import models
from django.core.files.storage import FileSystemStorage


fs = FileSystemStorage(
    location='/home/mircea/Work/djangoapp/bentoqa/screenshots/images')


class Domain(models.Model):
    url = models.CharField(max_length=512, default='')

    def __unicode__(self):
        return self.url


class Screenshot(models.Model):
    domain = models.ForeignKey(Domain)
    qa_image = models.ImageField(max_length=256, storage=fs, blank=True, null=True)
    production_image = models.ImageField(max_length=256, storage=fs, blank=True, null=True)
    run_id = models.IntegerField()
    date_taken = models.DateTimeField(default=lambda: datetime.datetime.now(
        pytz.timezone('Europe/Bucharest')))