#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Functions for the NetatmoAPRS Python Module."""

import time

import aprs.geo_util
import netatmoaprs
import lnetatmo

__author__ = 'Greg Albrecht W2GMD <gba@orionlabs.io>'
__license__ = 'Apache License, Version 2.0'
__copyright__ = 'Copyright 2016 Orion Labs, Inc.'


def get_weather(device_id, client_id, client_secret, username, password):
    weather = {}
    weather['wind_direction'] = '...'
    weather['wind_speed'] = '...'
    weather['gust'] = '...'
    weather['temperature'] = '...'
    weather['rain_1hr'] = '...'
    weather['rain_24hr'] = '...'
    weather['rain_midnight'] = '...'
    weather['humidity'] = '..'
    weather['pressure'] = '.....'

    #device_id = '70:ee:50:03:98:4c'  # Orion
    #device_id = '70:ee:50:02:be:74'  # Home

    authorization = lnetatmo.ClientAuth(
        client_id, client_secret, username, password)

    device_list = lnetatmo.DeviceList(authorization)
    if not device_id in device_list.stations:
        return
    device_data = device_list.stations[device_id]
    dashboard_data = device_data['dashboard_data']
    place_data = device_data['place']

    # Humidity is an acceptable format for APRS:
    weather['humidity'] = dashboard_data['Humidity']

    # Convert C to F for APRS:
    weather['temperature'] = netatmoaprs.c2f(dashboard_data['Temperature'])

    # Convert float to APRS format:
    if 'Pressure' in dashboard_data:
        weather['pressure'] = str(dashboard_data['Pressure']).replace('.', '')

    # Convert UTC Epoch to DHM Zulu:
    weather['timestamp'] = time.strftime(
        '%d%H%M', time.gmtime(dashboard_data['time_utc']))

    # Get location data and convert to APRS format:
    weather['latitude'] = aprs.geo_util.dec2dm_lat(place_data['location'][1])
    weather['longitude'] = aprs.geo_util.dec2dm_lng(place_data['location'][0])

    frame = "@%sz%s/%s_%s/%sg%st%03dr%sp%sP%sh%02db%sNttm" % (
        weather['timestamp'],
        weather['latitude'],
        weather['longitude'],
        weather['wind_direction'][:3],
        weather['wind_speed'][:3],
        weather['gust'][:3],
        weather['temperature'],
        weather['rain_1hr'][:3],
        weather['rain_24hr'][:3],
        weather['rain_midnight'][:3],
        weather['humidity'],
        weather['pressure'],
    )
    return frame


def run_doctest():  # pragma: no cover
    """Runs doctests for this module."""
    import doctest
    import netatmoaprs.util  # pylint: disable=W0406,W0621
    return doctest.testmod(netatmoaprs.util)


if __name__ == '__main__':
    run_doctest()  # pragma: no cover
