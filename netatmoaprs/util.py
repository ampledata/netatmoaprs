#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Utilities for the NetatmoAPRS Python Module."""

__author__ = 'Greg Albrecht W2GMD <gba@orionlabs.io>'
__license__ = 'Apache License, Version 2.0'
__copyright__ = 'Copyright 2016 Orion Labs, Inc.'


def c2f(t):
    """
    Converts Celsius Temperature to Fahrenheit Temperature.
    """
    return t * float(1.8000) + float(32.00)


def run_doctest():  # pragma: no cover
    """Runs doctests for this module."""
    import doctest
    import netatmoaprs.util  # pylint: disable=W0406,W0621
    return doctest.testmod(netatmoaprs.util)


if __name__ == '__main__':
    run_doctest()  # pragma: no cover
