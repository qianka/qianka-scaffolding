# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='{{ cookiecutter.repo_name }}',

    packages=find_packages(),

    install_requires=[
        'Flask',
        'celery',
        'redis',
        'mysqlclient',
        'msgpack-python',
        'qianka-flaskext',
        'qianka-sqlalchemy'
    ],
    setup_requires=[],
    tests_require=[],

    author="Qianka Inc."
)
