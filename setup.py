#!/usr/bin/env python


import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from setuptools import find_packages

version = '1.0.0'

specs = {
    'name' : 'clickanalysis',
    'version' : version,
    'description' : 'Django package to track all clicks across the site or email campaigns',
    'long_description' : 'Django package to track all clicks across the site or email campaigns',
    'url' : 'https://github.com/nitishkansal/django-clickanalysis',
    'author' : 'Nitish Kansal',
    'author_email' : 'tanu.kansal@gmail.com',
    'keywords' : ['click analysis', 'tracking'],
    'license' : 'BSD',
    'packages' : find_packages(),
    'classifiers' : (
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ),
}

if __name__=='__main__':
    setup(**specs)

