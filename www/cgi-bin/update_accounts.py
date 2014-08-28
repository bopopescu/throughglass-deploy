#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = 'yowenlove'

# enable debugging
import cgitb

cgitb.enable()

import sys
from ye2pack import pack_utils, works_pb2
from ye2pack.pack_pb2 import Packet
from ye2pack.works_pb2 import UpdateAccounts
from model import usr_info, bind_accounts


print "Content-Type: text/plain;charset=utf-8"
print

#
req_buf = sys.stdin.read()
req_pkt = pack_utils.pre_decode(buf=req_buf)
uin = req_pkt.uin

usr = usr_info.query(uin)
session = usr.get('session')

req_pkt = pack_utils.decode(buf=req_buf, key=session)
req = UpdateAccounts.Request()
req.ParseFromString(req_pkt.data)

for ba in req.bind_accounts:
    bind_accounts.update(
        uin=req.base_request.uin,
        openid=ba.openid,
        account_type=ba.type,
        access_token=ba.access_token,
        refresh_token=ba.refresh_token,
        expires_in=ba.expires_in,
        extra=ba.extra
    )

resp = UpdateAccounts.Response()
resp.base_response.err_code = works_pb2.ERR_NONE
resp_buf = pack_utils.encode(
    buf=resp.SerializeToString(),
    encrypt=Packet.CRYPT_NONE,
    key=session,
    uin=uin
)

print resp_buf