# -*- coding: utf-8 -*-

from lxml import etree
from lxml.builder import E
from .forms import CheckForm
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
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(BaseView, self).dispatch(*args, **kwargs)


class CheckOrderView(BaseView):
    def post(self, request, *args, **kwargs):
        form = CheckForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if form.check_md5(cd):
                payment = get_object_or_None(Payment,
                                             custome_number=cd['customerNumber'],
                                             scid=cd['scid'], shop_id=cd['shopId'])

                if payment:
                    now = datetime.now()

                    payment.performed_datetime = now
                    payment.save()

                    params = {'code': '0',
                              'shopId': str(cd['shopId']),
                              'invoiceId': str(cd['invoiceId']),
                              'performedDatetime': now.isoformat()}
                else:
                    params = {'code': '100'}
            else:
                params = {'code': '1'}

        else:
            params = {'code': '200'}

        element = E.checkOrderResponse(**params)
        content = etree.tostring(element,
                                 pretty_print=True,
                                 xml_declaration=True,
                                 encoding='UTF-8')

        return HttpResponse(content, content_type='application/xml')


class NoticeFormView(BaseView):
    def post(self, request, *args, **kwargs):
        return HttpResponse()
