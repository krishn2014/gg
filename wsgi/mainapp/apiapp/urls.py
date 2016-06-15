# apiapp
from django.conf.urls import patterns, include, url
# for including static content
# import imp, os.path

from views import *

# @deprecated
# from django.views.generic.simple import direct_to_template
# from django.shortcuts import render as direct_to_template

# Django REST framework
from rest_framework import routers

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mainapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # docs url
    # url(r'^$',root_page),
    url(r'^docs/', include('rest_framework_swagger.urls')),
)


# Django REST framework
# Wire up our API using automatic URL routing.
urlpatterns += patterns('',

    # apis
    url(r'^genres/$', GenresList.as_view()),
    url(r'^genres/(?P<pk>[0-9]+)/$', GenreDetail.as_view()),
    url(r'^tracks/$', TracksList.as_view()),
    url(r'^tracks/(?P<pk>[0-9]+)/$', TrackDetail.as_view()),
)
