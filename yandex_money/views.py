# -*- coding: utf-8 -*-

from lxml import etree
from lxml.builder import E
from .forms import CheckForm
from .forms import NoticeForm
from datetime import datetime
from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth import get_user_model
from annoying.functions import get_object_or_None
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import Payment

User = get_user_model()


class BaseView(View):
    form_class = None

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(BaseView, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if form.check_md5(cd):
                payment = self.get_payment(cd)
                params = self.get_response_params(payment, cd)
                self.mark_payment(payment, cd)
            else:
                params = {'code': '1'}
        else:
            params = {'code': '200'}

        content = self.get_xml(params)
        return HttpResponse(content, content_type='application/xml')

    def get_payment(self, cd):
        return get_object_or_None(Payment,
                                  custome_number=cd['customerNumber'],
                                  scid=cd['scid'], shop_id=cd['shopId'])

    def get_response_params(self, payment, cd):
        if payment:
            now = datetime.now()

            payment.performed_datetime = now
            payment.save()

            return {'code': '0',
                    'shopId': str(cd['shopId']),
                    'invoiceId': str(cd['invoiceId']),
                    'performedDatetime': now.isoformat()}
        return {'code': '100'}

    def mark_payment(self, payment, cd):
        pass

    def get_xml(self, params):
        element = E.checkOrderResponse(**params)
        return etree.tostring(element,
                              pretty_print=True,
                              xml_declaration=True,
                              encoding='UTF-8')


class CheckOrderFormView(BaseView):
    form_class = CheckForm


class NoticeFormView(BaseView):
    form_class = NoticeForm

    def mark_payment(self, payment, cd):
        payment.cps_email = cd.get('cps_email', '')
        payment.cps_phone = cd.get('cps_phone', '')
        payment.order_currency = cd.get('orderSumCurrencyPaycash')
        payment.shop_amount = cd.get('shopSumAmount')
        payment.shop_currency = cd.get('shopSumCurrencyPaycash')
        payment.payer_code = cd.get('paymentPayerCode')
        payment.payment_type = cd.get('paymentType')
        payment.status = payment.STATUS.SUCCESS
        payment.save()