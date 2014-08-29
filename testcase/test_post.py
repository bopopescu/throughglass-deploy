#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from ye2pack import pack_utils
from ye2pack import works_pb2
import rsa
import cgitb

cgitb.enable()


print "Content-Type: text/plain;charset=utf-8"
print

public_key = rsa.PublicKey(
    11176276734117980437, 65537)

client_ver = 0x10000000
uin = 100000

# build an auth request
post_req = works_pb2.Post.Request()
post_req.base_request.uin = uin
post_req.base_request.client_version = client_ver
post_req.media_id.append('asdasfdasdgafgadfas')
post_req.media_id.append('asgeewrq4t3gdfbe56rgsbdfs')
post_req.comment = 'test comment'

req_buf = pack_utils.encode(
    buf=post_req.SerializeToString(), key=public_key, cookie='cookie', version=client_ver,
    device_id='0123456789ABCDEF',
    encrypt=pack_utils.Packet.CRYPT_NONE, func_id=works_pb2.FUNCID_POST, ret_code=0, uin=uin)

print req_buf

import httplib

headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
# conn = httplib.HTTPConnection("throughglass.sourceforge.net")
conn = httplib.HTTPConnection("192.168.1.105:8080")
conn.request("POST", "/cgi-bin/post.py", req_buf, headers)
response = conn.getresponse()

if response.status == 200:
    resp_buf = response.read()

else:
    print('error code: %d' % response.status)
    exit(response.status)

conn.close()

print('[%s]' % resp_buf)
resp_pkt = pack_utils.decode(buf=resp_buf, key='password')

post_resp = works_pb2.Post.Response()
post_resp.ParseFromString(resp_pkt.data)

print('ret code: %d, id: %d' % (post_resp.base_response.err_code, post_resp.id))