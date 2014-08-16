from django.conf.urls import patterns, include, url
from django.views.decorators.cache import cache_page
from Apps.Blog.views import home, about, about_vblog, portfolio, contacts, search_articles, view_article
from Apps.Blog.feeds import ArticleFeed, PortfolioFeed

urlpatterns = patterns('',
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^$', home, name='Blog-home'),
    url(r'^about/$', cache_page(24 * 60 * 60)(about), name='Blog-about'),
    url(r'^about-vblog/$', cache_page(24 * 60 * 60)(about_vblog), name='Blog-about_vblog'),
    url(r'^portfolio/$', cache_page(1 * 60 * 60)(portfolio), name='Blog-portfolio'),
    url(r'^contacts/$', cache_page(24 * 60 * 60)(contacts), name='Blog-contacts'),
    url(r'^search/', search_articles),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^rss/blog/$', ArticleFeed(), name='Blog-articles_rss'),
    url(r'^rss/portfolio/$', PortfolioFeed(), name='Blog-portfolio_rss'),
    url(r'^(?P<slug>[\w-]+)/$', cache_page(24 * 60 * 60)(view_article), name='Blog-view_article'),
)