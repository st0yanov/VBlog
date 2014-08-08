from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from autoslug import AutoSlugField

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
