# -*- coding: utf-8 -*-

import os
from distutils.core import setup

__author__ = 'Alexey Kuzmin'
__version__ = '0.9'

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-yandex-money',
    version=__version__,
    packages=['yandex_money'],
    url='https://github.com/DrMartiner/django-yandex-money',
    license='MIT',
    author=__author__,
    author_email='DrMartiner@GMail.Com',
    description='Integrating django project with yandex-money',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        'Django>1.5',
        'South==0.8.4',
        'lxml==4.9.1',
        'django-webtest==1.7.7',
        'webtest==2.0.15',
        'django-annoying',
        'aniso8601',
    ],
)