# -*- coding: utf-8 -*-

from django.contrib import admin
from django.conf.urls import patterns, include, url
from app.views import OrderPage

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'payment-form/$', OrderPage.as_view(), name='payment_form'),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^yandex-money/', include('yandex_money.urls')),)
