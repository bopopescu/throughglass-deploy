#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = 'yowenlove'

from ye2pack import pack_utils
from ye2pack import works_pb2
import rsa
import base64
import cgitb

cgitb.enable()


print "Content-Type: text/plain;charset=utf-8"
print

public_key = rsa.PublicKey(
    11176276734117980437, 65537)

client_ver = 0x10000000
uin = 23232323

# build an auth request
auth_req = works_pb2.Auth.Request()
auth_req.base_request.uin = uin
auth_req.base_request.client_version = client_ver
auth_req.username = 'kirozhao'
auth_req.password = 'password'

req_buf = pack_utils.encode(
    buf=auth_req.SerializeToString(), key=public_key, cookie='cookie', version=client_ver,
    device_id='0123456789ABCDEF',
    encrypt=pack_utils.Packet.CRYPT_NONE, func_id=works_pb2.FUNCID_AUTH, ret_code=0, uin=uin)

# print req_buf

import httplib

headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
# conn = httplib.HTTPConnection("throughglass.sourceforge.net")
conn = httplib.HTTPConnection("192.168.1.105:8080")
conn.request("POST", "/cgi-bin/auth.py", req_buf, headers)
response = conn.getresponse()

if response.status == 200:
    resp_buf = response.read()

else:
    print('error code: %d' % response.status)
    exit(response.status)

conn.close()

print('[%s]' % resp_buf)
resp_pkt = pack_utils.decode(buf=resp_buf, key='password')

print('[%d]' % len(resp_pkt.data))
auth_resp = works_pb2.Auth.Response()
auth_resp.ParseFromString(resp_pkt.data)

print('ret code: %d, session: %s, uin: %d' % (auth_resp.base_response.err_code, auth_resp.session_key, auth_resp.uin))