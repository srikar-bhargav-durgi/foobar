from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
						url(r'^create_project$', views.create_project),
						url(r'^create_post$', views.create_post),
						url(r'^store_uid$', views.store_uid),
						url(r'^create_post_old$', views.redirect_post),
	)