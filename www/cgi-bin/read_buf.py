# -*- coding: UTF-8 -*-

import logging


def init(env):
    try:
        cl = int(env.get('CONTENT_LENGTH', 0))

    except (ValueError):
        cl = 0

    logging.basicConfig(level=logging.DEBUG)
    return env['wsgi.input'].read(cl)


def finish(start_response, resp_buf):
    # start response
    response_headers = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(len(resp_buf)))
    ]
    start_response('200 OK', response_headers)
    return [resp_buf]