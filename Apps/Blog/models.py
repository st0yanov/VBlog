from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from autoslug import AutoSlugField

import os, time

# Create your models here.

class Article(models.Model):
    author = models.ForeignKey(User, null=True, blank=True)
    slug = AutoSlugField(unique=True, populate_from='title')
    title = models.CharField(max_length=128)
    content = RichTextField()
    tags = models.CharField(max_length=128)
    pub_date = models.DateTimeField()
    published = models.BooleanField(default=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return '/%s' % self.slug

def generate_filename(instance, old_filename):
    ext = os.path.splitext(old_filename)[1]
    filename = str(time.time())+ext

    return 'portfolio/' + filename

class Portfolio(models.Model):
    title = models.CharField(max_length=128)
    url = models.URLField()
    description = RichTextField()
    technologies = models.CharField(max_length=256)
    screenshot = models.ImageField(upload_to=generate_filename)
    pub_date = models.DateTimeField()

    def __unicode__(self):
        return self.title