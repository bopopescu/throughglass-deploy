#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = 'yowenlove'


# enable debugging
import cgitb

cgitb.enable()

import sys

req_buf = sys.stdin.read()

from ye2pack import pack_utils
from ye2pack import works_pb2
import rsa

print "Content-Type: text/plain;charset=utf-8"
print


