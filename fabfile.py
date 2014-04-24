# -*- coding: utf-8 -*-

from fabric.api import *


@task
def push():
    local('git push')


@task
def upload():
    local('python setup.py sdist upload')
