from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^$', 'Apps.Blog.views.home', name='Blog-home'),
    url(r'^about/$', 'Apps.Blog.views.about', name='Blog-about'),
    url(r'^about-vblog/$', 'Apps.Blog.views.about_vblog', name='Blog-about_vblog'),
    url(r'^portfolio/$', 'Apps.Blog.views.portfolio', name='Blog-portfolio'),
    url(r'^contacts/$', 'Apps.Blog.views.contacts', name='Blog-contacts'),
    url(r'^(?P<slug>[\w-]+)/$', 'Apps.Blog.views.view_article', name='Blog-view_article'),
)