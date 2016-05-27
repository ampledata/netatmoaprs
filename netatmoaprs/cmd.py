#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""NetatmoAPRS commands."""

__author__ = 'Greg Albrecht W2GMD <gba@orionlabs.io>'
__copyright__ = 'Copyright 2016 Orion Labs, Inc.'
__license__ = 'All rights reserved. Do not redistribute.'


import argparse

import aprs
import netatmoaprs


def cli():
    """Command Line interface for APRS."""

    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-c', '--callsign', help='callsign', required=True
    )
    parser.add_argument(
        '-p', '--passcode', help='passcode', required=True
    )
    parser.add_argument(
        '-u', '--ssid', help='ssid', default='1'
    )

    # Netatmo API Params
    parser.add_argument(
        '-D', '--device_id',
        help='Netatmo Weather Station Device ID (MAC Address)', required=True
    )
    parser.add_argument(
        '-C', '--client_id',
        help='Netatmo API Client ID', required=True
    )
    parser.add_argument(
        '-S', '--client_secret',
        help='Netatmo API Client ID', required=True
    )
    parser.add_argument(
        '-U', '--netatmo_username',
        help='Netatmo API Username', required=True
    )
    parser.add_argument(
        '-P', '--netatmo_password',
        help='Netatmo API Password', required=True
    )

    opts = parser.parse_args()

    aprs_i = aprs.APRS(opts.callsign, opts.passcode)
    aprs_i.connect()

    src_callsign = aprs.util.full_callsign(
        {'callsign': opts.callsign, 'ssid': opts.ssid})

    weather_frame = netatmoaprs.get_weather(
        opts.device_id,
        opts.client_id,
        opts.client_secret,
        opts.netatmo_username,
        opts.netatmo_password
    )
    aprs_i.send("%s>APRS:%s" % (src_callsign, weather_frame))
