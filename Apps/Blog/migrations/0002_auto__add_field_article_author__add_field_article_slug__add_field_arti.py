# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Article.author'
        db.add_column(u'Blog_article', 'author',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Adding field 'Article.slug'
        db.add_column(u'Blog_article', 'slug',
                      self.gf('django.db.models.fields.CharField')(default='test', max_length=128),
                      keep_default=False)

        # Adding field 'Article.tags'
        db.add_column(u'Blog_article', 'tags',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=128),
                      keep_default=False)

        # Adding field 'Article.published'
        db.add_column(u'Blog_article', 'published',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)


        # Changing field 'Article.title'
        db.alter_column(u'Blog_article', 'title', self.gf('django.db.models.fields.CharField')(max_length=128))

    def backwards(self, orm):
        # Deleting field 'Article.author'
        db.delete_column(u'Blog_article', 'author')

        # Deleting field 'Article.slug'
        db.delete_column(u'Blog_article', 'slug')

        # Deleting field 'Article.tags'
        db.delete_column(u'Blog_article', 'tags')

        # Deleting field 'Article.published'
        db.delete_column(u'Blog_article', 'published')


        # Changing field 'Article.title'
        db.alter_column(u'Blog_article', 'title', self.gf('django.db.models.fields.CharField')(max_length=96))

    models = {
        u'Blog.article': {
            'Meta': {'object_name': 'Article'},
            'author': ('django.db.models.fields.IntegerField', [], {}),
            'content': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'tags': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['Blog']