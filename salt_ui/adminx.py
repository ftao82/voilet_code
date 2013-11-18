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
from django.contrib import admin
import xadmin
from xadmin import views
from models import  AccessRecord
from xadmin.layout import Main, TabHolder, Tab, Fieldset, Row, Col, AppendedText, Side
from xadmin.plugins.inline import Inline
from xadmin.plugins.batch import BatchChangeAction


class MaintainInline(object):
    extra = 1
    style = 'accordion'


class PostAdmin(object):
    def open_detail(self,instance):
        return  "<a href='http://***/%s' target='_blank'>详情</a>" % instance.Host
    list_display = ('user_name','title','Discovery_date','Occur_date','Solve_date','Source')
    search_fields = ('title','user_name')
    exclude = ('user_name',)
    def save_models(self):
        #print dir(self)
        self.new_obj.user_name = self.request.user
        super(PostAdmin,self).save_models()






class PosterAdmin(object):
    list_display = ('name', 'email',)
    search_fields = ('name', 'email')

class Poster_OP(object):
    list_display = ('name',)
    search_fields = ('name',)

class AccessRecordAdmin(object):
    def avg_count(self, instance):
        return int(instance.view_count / instance.user_count)
    avg_count.short_description = "Avg Count"
    avg_count.allow_tags = True
    avg_count.is_column = True

    list_display = ('test')




xadmin.site.register(AccessRecord,AccessRecordAdmin)