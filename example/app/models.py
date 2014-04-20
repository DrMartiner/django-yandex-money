# -*- coding: utf-8 -*-

from django.db import models
from django.template.defaultfilters import truncatechars


class Goods(models.Model):
    name = models.CharField('Наименование', max_length=32)
    price = models.PositiveIntegerField('Стоимость')

    def __unicode__(self):
        return '%s %d' % (truncatechars(self.name, 8),
                          self.price)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Order(models.Model):
    goods = models.ForeignKey(Goods, verbose_name='Товар')
    count = models.PositiveIntegerField('Кол-во', default=1)
    payment = models.ForeignKey('yandex_money.Payment',
                                verbose_name='Платеж')
    amount = models.PositiveIntegerField('Сумма заказа')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'