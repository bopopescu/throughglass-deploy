# -*- coding: UTF-8 -*-
__author__ = 'guang_hik'


def read(env):
	try:
		cl = int(environ.get('CONTENT_LENGTH', 0))
	except (ValueError):
		cl = 0

	return env['wsgi.input'].read(cl)

