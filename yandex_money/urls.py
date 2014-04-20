# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import NoticeFormView
from .views import CheckOrderView


urlpatterns = patterns('',
    url(r'^check/', CheckOrderView.as_view(), name='yandex_money_check'),
    url(r'^notice/', NoticeFormView.as_view(), name='yandex_money_notice'),
)
urlpatterns += staticfiles_urlpatterns()