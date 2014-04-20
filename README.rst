django-yandex-money
===================


Установка
---------

#.  Установить пакет `pypi`__ using `pip`__:

    .. code:: sh

        pip install django-yandex-money

#.  Добавить `yandex_money` в `settings.INSTALLED_APPS`__:

    .. code:: python

        INSTALLED_APPS = (
            ...
            yandex_money,
            ...
        )

#. Выполнить синхронизацию с БД:__:

    .. code:: sh

        python manage.py syncdb
        python manage.py migrate # для тех, кто использует south

#. Добавить в `urls.py`__:

    .. code:: python

    urlpatterns = patterns('',
        # ...
        url(r'^fail-payment/$', TemplateView.as_view(template_name='fail.html'), name='payment_fail'),
        url(r'^success-payment/$', TemplateView.as_view(template_name='success.html'), name='payment_success'),
        url(r'^yandex-money/', include('yandex_money.urls')),
    )

#. Указать в `settings` следующие параметры__:

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

