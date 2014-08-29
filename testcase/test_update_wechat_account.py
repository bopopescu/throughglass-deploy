#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = 'yowenlove'

# enable debugging
import cgitb

cgitb.enable()

from ye2pack import pack_utils, works_pb2
from ye2pack.works_pb2 import UpdateWeChatAccount
from ye2pack.pack_pb2 import Packet

print "Content-Type: text/plain;charset=utf-8"
print

client_ver = 0x10000000
uin = 100000

req = UpdateWeChatAccount.Request()
req.base_request.uin = uin
req.base_request.client_version = client_ver
req.code = 'xxxyyy'

req_buf = pack_utils.encode(
    buf=req.SerializeToString(),
    encrypt=Packet.CRYPT_NONE,
    key='asdf',
    uin=req.base_request.uin
)

import httplib

headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
# conn = httplib.HTTPConnection("throughglass.sourceforge.net")
conn = httplib.HTTPConnection("192.168.1.105:8080")
conn.request("POST", "/cgi-bin/update_wechat_account.py", req_buf, headers)
response = conn.getresponse()

if response.status == 200:
    resp_buf = response.read()

else:
    print('error code: %d' % response.status)
    exit(response.status)

conn.close()

print('[%s]' % resp_buf)
resp_pkt = pack_utils.decode(buf=resp_buf, key='password')

resp = UpdateWeChatAccount.Response()
resp.ParseFromString(resp_pkt.data)

print('ret code: %d' % resp.base_response.err_code)
