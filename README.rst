django-yandex-money
===================


Установка
---------

#.  Установить пакет:

    .. code:: sh

        pip install django-yandex-money

#.  Добавить ``yandex_money`` в ``settings.INSTALLED_APPS``:

    .. code:: python

        INSTALLED_APPS = (
            ...
            'yandex_money',
            ...
        )

#. Выполнить синхронизацию с БД:

    .. code:: sh

        python manage.py syncdb
        python manage.py migrate # для тех, кто использует south

#. Добавить в ``urls.py``:

    .. code:: python

        urlpatterns = patterns('',
            # ...
            url(r'^fail-payment/$', TemplateView.as_view(template_name='fail.html'), name='payment_fail'),
            url(r'^success-payment/$', TemplateView.as_view(template_name='success.html'), name='payment_success'),
            url(r'^yandex-money/', include('yandex_money.urls')),
        )

#. Указать в settings следующие параметры:

    .. code:: python

        YANDEX_MONEY_DEBUG = False
        YANDEX_MONEY_SCID = 12345
        YANDEX_MONEY_SHOP_ID = 56789
        YANDEX_MONEY_SHOP_PASSWORD = 'password'
        YANDEX_MONEY_FAIL_URL = 'https://example.com/fail-payment/'
        YANDEX_MONEY_SUCCESS_URL = 'https://example.com/success-payment/'


#. Указать в рабочем Яндекс-денег кабинете натсрйоки для приема уведомлений:

* paymentAvisoURL: https://example.com/yandex-money/aviso/
* checkURL: https://example.com/yandex-money/check/
* failURL: https://example.com/fail-payment/
* successURL: https://example.com/success-payment/


Использование
-------------

. _Полный пример использования: https://github.com/DrMartiner/django-yandex-money/tree/develop/example

#. Представление платежной формы:

    .. code:: python

        # -*- coding: utf-8 -*-

        from django.views.generic import TemplateView
        from yandex_money.forms import PaymentForm
        from yandex_money.models import Payment


        class OrderPage(TemplateView):
            template_name = 'order_page.html'

            def get_context_data(self, **kwargs):
                payment = Payment(order_amount=123)
                payment.save()

                ctx = super(OrderPage, self).get_context_data(**kwargs)
                ctx['form'] = PaymentForm(instance=payment)
                return ctx

#. Шаблон платежной формы:

    .. code:: html

        <html>
            <head>
                <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
                <meta charset="utf-8">
            </head>
            <body>
                <div style="border: 1px dotted gray; padding: 15px 15px 0; margin: 30px auto; width: 300px;">
                    <form name="ShopForm" method="POST" action="https://yandex.ru/eshop.xml">
                        <ul style="list-style: none;">
                            <li style="margin-bottom: 20px;">
                                Сумма заказа: <b>{{ form.sum.value }}</b>
                            </li>

                            {{ form.as_ul|safe }}

                            <li style="margin-top: 20px;">
                                <input type="submit" value="Оплатить">
                            </li>
                        </ul>
                    </form>
                </div>
            </body>
        </html>