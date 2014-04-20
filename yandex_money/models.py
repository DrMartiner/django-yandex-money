# -*- coding: utf-8 -*-

from uuid import uuid4
from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()


class Payment(models.Model):
    class STATUS:
        PROCESSED = 'processed'
        SUCCESS = 'success'
        FAIL = 'fail'

        CHOICES = (
            (PROCESSED, 'Processed'),
            (SUCCESS, 'Success'),
            (FAIL, 'Fail'),
        )

    class PAYMENT_TYPE:
        PC = 'pc'
        AC = 'ac'
        GP = 'gp'
        MC = 'mc'

        CHOICES = (
            (PC, 'Яндекс.Деньги'),
            (AC, 'Банковская карта'),
            (GP, 'По коду через терминал'),
            (MC, 'со счета мобильного телефона'),
        )

    class CURRENCY:
        RUB = 643
        TEST = 10643

        CHOICES = (
            (RUB, 'Рубли'),
            (TEST, 'Тестовая валюта'),
        )

    user = models.ForeignKey(User, blank=True, null=True,
                             verbose_name='Пользователь')
    custome_number = models.CharField('Номер заказа',
                                      unique=True, max_length=64,
                                      default=lambda: str(uuid4()).replace('-', ''))
    status = models.CharField('Результата', max_length=16,
                              choices=STATUS.CHOICES,
                              default=STATUS.PROCESSED)

    scid = models.PositiveIntegerField('Номер витрины',
                                       default=settings.YANDEX_MONEY_SCID)
    shop_id = models.PositiveIntegerField('ID магазина',
                                          default=settings.YANDEX_MONEY_SHOP_ID)
    payment_type = models.CharField('Способ платежа', max_length=2,
                                    default=PAYMENT_TYPE.PC,
                                    choices=PAYMENT_TYPE.CHOICES)
    invoice_id = models.PositiveIntegerField('Номер транзакции оператора',
                                             blank=True, null=True)
    order_amount = models.FloatField('Сумма заказа')
    shop_amount = models.DecimalField('Сумма полученная на р/с',
                                      max_digits=5,
                                      decimal_places=2,
                                      blank=True, null=True,
                                      help_text='За вычетом процента оператора')

    order_currency = models.PositiveIntegerField('Валюта',
                                                 default=CURRENCY.RUB,
                                                 choices=CURRENCY.CHOICES)
    shop_currency = models.PositiveIntegerField('Валюта полученная на р/с',
                                                blank=True, null=True,
                                                default=CURRENCY.RUB,
                                                choices=CURRENCY.CHOICES)
    payer_code = models.CharField('Номер виртуального счета',
                                  max_length=33,
                                  blank=True, null=True)

    success_url = models.URLField('URL успешной оплаты',
                                  default=settings.YANDEX_MONEY_SUCCESS_URL)
    fail_url = models.URLField('URL неуспешной оплаты',
                               default=settings.YANDEX_MONEY_FAIL_URL)

    cps_email = models.EmailField('Почты плательщика', blank=True, null=True)
    cps_phone = models.CharField('Телефон плательщика', max_length=15, blank=True, null=True)

    pub_date = models.DateTimeField('Время создания', auto_now_add=True)
    performed_datetime = models.DateTimeField('Выполнение запроса', blank=True, null=True)

    @property
    def is_payed(self):
        return getattr(self, 'status', '') == self.STATUS.SUCCESS

    class Meta:
        ordering = ('pub_date',)
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'
