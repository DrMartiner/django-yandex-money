# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import Goods
from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ('goods', 'count', 'payment', 'amount')
    list_filter = ('goods', )

admin.site.register(Goods)
admin.site.register(Order, OrderAdmin)