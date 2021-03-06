#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Setup for the NetatmoAPRS Python Module.

Source:: https://github.com/ampledata/netatmoaprs
"""


__title__ = 'netatmoaprs'
__version__ = '0.0.3'
__author__ = 'Greg Albrecht W2GMD <gba@orionlabs.io>'
__license__ = 'Apache License, Version 2.0'
__copyright__ = 'Copyright 2016 Orion Labs, Inc.'


import os
import setuptools
import sys


def publish():
    """Function for publishing package to pypi."""
    if sys.argv[-1] == 'publish':
        os.system('python setup.py sdist upload')
        sys.exit()


publish()


setuptools.setup(
    name='netatmoaprs',
    version=__version__,
    description='Netatmo to APRS Publisher for Weather data.',
    author='Greg Albrecht',
    author_email='gba@orionlabs.io',
    packages=['netatmoaprs'],
    package_data={'': ['LICENSE']},
    license=open('LICENSE').read(),
    long_description=open('README.rst').read(),
    url='https://github.com/ampledata/netatmoaprs',
    install_requires=['aprs'],
    package_dir={'netatmoaprs': 'netatmoaprs'},
    zip_safe=False,
    include_package_data=True,
    entry_points={'console_scripts': ['netatmoaprs = netatmoaprs.cmd:cli']}
)
