#!/usr/bin/env python
#-*- coding: utf-8 -*-
#=============================================================================
#     FileName:
#         Desc:
#       Author: 苦咖啡
#        Email: voilet@qq.com
#     HomePage: http://blog.kukafei520.net
#      Version: 0.0.1
#   LastChange: 
#      History:
#=============================================================================

from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
import xadmin
import salt_ui.views.index
import salt_ui.urls
xadmin.autodiscover()

# from xadmin.plugins import xversion
# xversion.registe_models()

urlpatterns = patterns('',
    #salt_ui
    url(r'(?P<id>\d+)/$',salt_ui.views.index.salt_status),
    url(r'',salt_ui.views.index.salt_index),
    #url(r'^$','salt_ui.views.index.auto'),
    #url(r'^overview$','salt_ui.views.index.overview'),
    #url(r'^minions$','salt_ui.views.index.minions'),
    #url(r'^minion$','salt_ui.views.index.minion'),
    #url(r'^execute$','salt_ui.views.index.execute'),
    #url(r'^detail$','salt_ui.views.index.detail'),
    #url(r'^getjobinfo$','salt_ui.views.index.getjobinfo'),
    #url(r'^service$','salt_ui.views.index.service'),
)


