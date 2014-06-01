from django.conf.urls import patterns, include, url
from whiteboard.views import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/','whiteboard.views.home_view'),
    url(r'^whiteboard/(?P<id>\d+)/$','whiteboard.views.view_message'),
    url(r'^whiteboard/filter/(?P<term>[\w ]+)/$','whiteboard.views.filter_messages'),
    url(r'^whiteboard/users/(?P<username>\w+)/$','whiteboard.views.filter_msg_user'),
    url(r'^whiteboard/post', 'whiteboard.views.post_message'),
    url(r'^login/', 'whiteboard.views.login_user'),
    url(r'^logout/', 'whiteboard.views.logout_user'),
    url(r'^register/', 'whiteboard.views.register_user'),
)
