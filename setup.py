# -*- coding: utf-8 -*-
from __future__ import with_statement

from setuptools import setup


version = '1.1.3'


setup(
    name='django-json-response',
    version=version,
    keywords='django-json-response django-jsonp-response',
    description="DIY Django's JsonResponse and JsonpResponse",
    long_description=open('README.rst').read(),

    url='https://github.com/Brightcells/django-json-response',

    author='Hackathon',
    author_email='kimi.huang@brightcells.com',

    py_modules=['json_response'],
    install_requires=[],

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Office/Business :: Financial :: Spreadsheet',
    ],
)
