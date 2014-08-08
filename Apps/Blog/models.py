from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=96)
    pub_date = models.DateTimeField()
    content = models.TextField()

    def __unicode__(self):
        return self.name
