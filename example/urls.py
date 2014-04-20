# -*- coding: utf-8 -*-

from django.contrib import admin
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView
from app.views import OrderPage

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'payment-form/$', OrderPage.as_view(), name='payment_form'),
                       url(r'fail-payment/$', TemplateView.as_view(template_name='fail.html'), name='payment_fail'),
                       url(r'success-payment/$', TemplateView.as_view(template_name='success.html'), name='payment_success'),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^yandex-money/', include('yandex_money.urls')),)

urlpatterns += staticfiles_urlpatterns()