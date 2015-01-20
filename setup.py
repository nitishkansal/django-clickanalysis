#!/usr/bin/env python


import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


specs = {
    'name' : 'clickanalysis',
    'version' : '1.0.0',
    'description' : 'Django package to track all clicks in email campaigns',
    'long_description' : 'Django package to track all clicks in email campaigns',
    'url' : 'https://github.com/nitishkansal',
    'author' : 'Nitish Kansal',
    'author_email' : 'tanu.kansal@gmail.com',
    'keywords' : ['click analysis', 'tracking'],
    'license' : 'BSD',
    'packages' : ['clickanalysis'],
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

