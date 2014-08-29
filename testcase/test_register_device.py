# !/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = 'yowenlove'

from ye2pack import pack_utils
from ye2pack import works_pb2

import rsa

public_key = rsa.PublicKey(
	11176276734117980437, 65537)

client_ver = 0x10000000
uin = 23232323

# build an auth request
req = works_pb2.RegisterDevice.Request()
req.base_request.uin = uin
req.base_request.client_version = client_ver
req.device_id = 'AA:BB:CC:DD:EE:FF'

req_buf = pack_utils.encode(buf=req.SerializeToString(), key=public_key, cookie='cookie', version=client_ver,
							device_id='0123456789ABCDEF',
							encrypt=pack_utils.Packet.CRYPT_NONE)

print req_buf

import httplib

headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
# conn = httplib.HTTPConnection("throughglass.sourceforge.net")
conn = httplib.HTTPConnection("api.throughglass.sf.net")
conn.request("POST", "/cgi-bin/register_device.py", req_buf, headers)
response = conn.getresponse()

if response.status == 200:
	resp_buf = response.read()

else:
	print('error code: %d' % response.status)
	exit(response.status)

conn.close()

print('[%s]' % resp_buf)
resp_pkt = pack_utils.decode(buf=resp_buf, key='password')
resp = works_pb2.RegisterDevice.Response()
resp.ParseFromString(resp_pkt.data)

print('ret code: %d, username: %s, uin: %d' % (resp.base_response.err_code, resp.username, resp.uin))