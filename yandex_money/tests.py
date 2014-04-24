# -*- coding: utf-8 -*-

from lxml import etree
from django.conf import settings
from django_webtest import WebTest
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model
from yandex_money.forms import BasePaymentForm
from django.test.utils import override_settings
from yandex_money.models import Payment

User = get_user_model()


class CheckPaymentTest(WebTest):
    params = {
        'scid': str(settings.YANDEX_MONEY_SCID),
        'requestDatetime': '2011-05-04T20:38:00.000+04:00',
        'action': 'checkOrder',
        'shopId': str(settings.YANDEX_MONEY_SHOP_ID),
        'shopArticleId': '456',
        'invoiceId': '1234567',
        'orderCreatedDatetime': '2011-05-04T20:38:00.000+04:00',
        'orderSumAmount': '87.10',
        'orderSumCurrencyPaycash': '643',
        'orderSumBankPaycash': '1001',
        'shopSumAmount': '86.23',
        'shopSumCurrencyPaycash': '643',
        'shopSumBankPaycash': '1001',
        'paymentPayerCode': '42007148320',
        'paymentType': 'GP',
    }

    def setUp(self):
        self.url = reverse('yandex_money_check')

        self.payment = Payment(order_amount=87.1)
        self.payment.save()

    def test_check(self):
        params = self.params.copy()
        params['customerNumber'] = self.payment.custome_number
        params['md5'] = BasePaymentForm.make_md5(params)

        res = self.app.post(self.url, params=params)

        self.assertEquals(res.content_type, 'application/xml',
                          'Content type is not XML')

        attrs = etree.fromstring(res.content).attrib
        self.assertEquals(attrs['code'], '0', 'Code is not success')
        self.assertEquals(attrs['shopId'], params['shopId'],
                          'ShopID is not valid')
        self.assertEquals(attrs['invoiceId'], params['invoiceId'],
                          'InvoiceId is not valid')
        self.assertEquals(len(attrs), 4, 'Response has excess attrs')

    def test_bad_md5(self):
        params = self.params.copy()
        params['customerNumber'] = self.payment.custome_number
        params['md5'] = '202CB962AC59075B964B07152D234B71'

        res = self.app.post(self.url, params=params)

        attrs = etree.fromstring(res.content).attrib
        self.assertEquals(attrs['code'], '1',
                          'The checking md5 was wrong. Code is not "1"')
        self.assertEquals(len(attrs), 1, 'Response has excess attrs')

    def test_bad_data(self):
        params = self.params.copy()
        params['customerNumber'] = self.payment.custome_number
        params['scid'] = 100500
        params['md5'] = BasePaymentForm.make_md5(params)

        res = self.app.post(self.url, params=params)

        attrs = etree.fromstring(res.content).attrib
        self.assertEquals(attrs['code'], '200',
                          'Code is not "200"')
        self.assertEquals(len(attrs), 1, 'Response has excess attrs')


class NoticePaymentTest(WebTest):
    params = {
        'scid': str(settings.YANDEX_MONEY_SCID),
        'requestDatetime': '2011-05-04T20:38:00.000+04:00',
        'action': 'paymentAviso',
        'shopId': str(settings.YANDEX_MONEY_SHOP_ID),
        'shopArticleId': '456',
        'invoiceId': '1234567',
        'orderCreatedDatetime': '2011-05-04T20:38:00.000+04:00',
        'orderSumAmount': '87.10',
        'orderSumCurrencyPaycash': '643',
        'orderSumBankPaycash': '1001',
        'shopSumAmount': '86.23',
        'shopSumCurrencyPaycash': '643',
        'shopSumBankPaycash': '1001',
        'paymentPayerCode': '42007148320',
        'paymentType': 'GP',
    }

    def setUp(self):
        self.payment = Payment(order_amount=87.1)
        self.payment.save()

        self.url = reverse('yandex_money_check')

    def test_notice(self):
        params = self.params.copy()
        params['customerNumber'] = self.payment.custome_number
        params['md5'] = BasePaymentForm.make_md5(params)

        res = self.app.post(self.url, params=params)

        self.assertEquals(res.content_type, 'application/xml',
                          'Content type is not XML')

        attrs = etree.fromstring(res.content).attrib
        self.assertEquals(attrs['code'], '0', 'Code is not success')
        self.assertEquals(attrs['shopId'], params['shopId'],
                          'ShopID is not valid')
        self.assertEquals(attrs['invoiceId'], params['invoiceId'],
                          'InvoiceId is not valid')
        self.assertEquals(len(attrs), 4, 'Response has excess attrs')

        payment = Payment.objects.get(pk=self.payment.pk)
        self.assertEquals(str(payment.order_currency),
                          params['orderSumCurrencyPaycash'])
        self.assertEquals(str(payment.shop_amount),
                          params['shopSumAmount'])
        self.assertEquals(str(payment.shop_currency),
                          params['shopSumCurrencyPaycash'])
        self.assertEquals(payment.payer_code,
                          params['paymentPayerCode'])
        self.assertEquals(payment.payment_type,
                          params['paymentType'])


class Md5HashTest(WebTest):
    @override_settings(YANDEX_MONEY_SHOP_PASSWORD='s<kY23653f,{9fcnshwq')
    def test_md5_sign(self):
        cd = {
            'action': 'checkOrder',
            'orderSumAmount': '87.10',
            'orderSumCurrencyPaycash': '643',
            'orderSumBankPaycash': '1001',
            'shopId': '13',
            'invoiceId': '55',
            'customerNumber': '8123294469',
            'md5': '1B35ABE38AA54F2931B0C58646FD1321',
        }
        res = BasePaymentForm.check_md5(cd)
        self.assertTrue(res, 'MD5 sign is not valid')