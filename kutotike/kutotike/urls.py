from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from forum.views import index,new_post,list_posts,delete_post,edit_post,delete_topic

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'kutotike.views.home', name='home'),
    # url(r'^kutotike/', include('kutotike.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/',index),
    url(r'^post/$',new_post),
    url(r'^post\?tid=(?P<tid>\d+)/$',list_posts),
    url(r'^post\?tid=(?P<tid>\d+)\?delete/$',delete_topic),
    url(r'^post\?tid=(?P<tid>\d+)\?pid=(?P<pid>\d+)\?reply/$',new_post),
    url(r'^post\?tid=(?P<tid>\d+)\?pid=(?P<pid>\d+)\?delete/$',delete_post),
    url(r'^post\?tid=(?P<tid>\d+)\?pid=(?P<pid>\d+)\?edit/$',edit_post),
)
