from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'Apps.Blog.views.home', name='Blog-home'),
    url(r'^about/$', 'Apps.Blog.views.about', name='Blog-about'),
    url(r'^contacts/$', 'Apps.Blog.views.contacts', name='Blog-contacts'),
)