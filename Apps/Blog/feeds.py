# -*- coding: utf-8 -*- 

from django.contrib.syndication.views import Feed
from Apps.Blog.models import Article, Portfolio
from django.core.urlresolvers import reverse

class ArticleFeed(Feed):
    title = 'Последни статии от блога на Веско'
    link = '/'
    description = 'Фийда се обновява автоматично при добавяне или променяне на статии.'

    def items(self):
        return Article.objects.all().order_by('-pub_date')[:30]

    def item_title(self, item):
        return item.title

    def item_link(self, item):
        return item.get_absolute_url()

    def item_description(self, item):
        return item.content

    def item_pubdate(self, item):
        return item.pub_date

    def item_categories(self, item):
        tags = item.tags.split(',')
        return [tag.strip() for tag in tags]

    def item_author_name(self, item):
        return item.author.username

class PortfolioFeed(Feed):
    title = 'Последни проекти на Веско'
    link = '/portfolio/'
    description = 'Фийда се обновява автоматично при добавяне или променяне на проект.'

    def get_object(self, request, *args, **kwargs):
        self.request = request

    def items(self):
        return Portfolio.objects.all().order_by('-pub_date')[:30]

    def item_title(self, item):
        return item.title

    def item_link(self, item):
        return item.url

    def item_description(self, item):
        return item.description

    def item_pubdate(self, item):
        return item.pub_date

    def item_categories(self, item):
        technologies = item.technologies.split(',')
        return [technology.strip() for technology in technologies]

    def item_enclosure_url(self, item):
        if item.screenshot:
            url = item.screenshot.url
        else:
            url = None
        return self.request.build_absolute_uri(reverse('Blog-home'))[:-1]+url if url else None