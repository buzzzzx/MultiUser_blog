# -*- coding: utf-8 -*-
__author__ = 'buzz'
__date__ = '2017/11/9 下午7:26'

from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^$', views.post_list, name='post_list'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[a-zA-Z0-9]{8})/$', views.post_detail, name='post_detail'),
    url(r'^write/$', views.post_write, name='post_write'),
    # tag
    url(r'^tag/(?P<tag_slug>[-\w]+)/$', views.post_list, name='post_list_by_tag')
]
