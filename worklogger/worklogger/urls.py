from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'worklogger.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                    url(r'^feed/', include('feed.urls')),
				    url(r'^admin/', include(admin.site.urls)),
				    url(r'^create_post/', include('create_post.urls')),
    				)

