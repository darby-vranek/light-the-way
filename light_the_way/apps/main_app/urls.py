from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'^select/(?P<tag_id>[0-9]+)-(?P<active_search>[0-9_]*)$', views.select),
	url(r'^show/(?P<tag_ids>[0-9_]*)/$', views.show),
	url(r'^show/$', views.show_all)
]
