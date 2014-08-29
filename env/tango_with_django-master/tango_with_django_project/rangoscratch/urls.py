from django.conf.urls import patterns, url
from rangoscratch import views
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('', url(r'^$', views.index, name='index'),
                           url(r'^test/$', views.test, name='test'),
                           url(r'^about/$', views.about, name='about'),
                           url(r'^add_category/$', views.add_category, name='add_category'),
                           url(r'^category/(?P<category_name_url>\w+)$', views.category, name='category'),)

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )
