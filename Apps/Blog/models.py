from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from autoslug import AutoSlugField
from django.core.urlresolvers import reverse

from helpers import expire_view_cache

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
        return reverse('Blog-view_article', args=[self.slug])

    def save(self, *args, **kwargs):
        try:
            item = Article.objects.get(slug=self.slug)
            expire_view_cache('Blog-view_article', [self.slug])
        except Article.DoesNotExist:
            pass
        expire_view_cache('Blog-home')
        super(Article, self).save(*args, **kwargs)

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

    def save(self, *args, **kwargs):
        try:
            item = Portfolio.objects.get(id=self.id)
            if item.screenshot != self.screenshot:
                item.screenshot.delete(save=False)
        except Portfolio.DoesNotExist:
            pass

        expire_view_cache('Blog-portfolio')
        super(Portfolio, self).save(*args, **kwargs)