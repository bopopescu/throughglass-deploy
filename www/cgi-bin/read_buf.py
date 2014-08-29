# -*- coding: UTF-8 -*-
__author__ = 'guang_hik'


def read(env):
    try:
        cl = int(env.get('CONTENT_LENGTH', 0))
    except (ValueError):
        cl = 0

    return env['wsgi.input'].read(cl)


def write(start_response, resp_buf):
    # start response
    response_headers = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(len(resp_buf)))
    ]
    start_response('200 OK', response_headers)
    return [resp_buf]