# -*- coding: UTF-8 -*-


from ye2pack import pack_utils, works_pb2
from ye2pack.works_pb2 import Auth
from ye2pack.pack_pb2 import Packet
import rsa
import read_buf
import logging


def process(req_buf):
    private_key = rsa.PrivateKey(
        11176276734117980437, 65537, 6939363295624337393, 12879322847, 867768971)

    req_pkt = pack_utils.decode(buf=req_buf, key=private_key)
    auth_req = Auth.Request()
    auth_req.ParseFromString(req_pkt.data)

    logging.debug('request username = %s, password = %s' % (auth_req.username, auth_req.password))

    auth_resp = Auth.Response()
    auth_resp.base_response.err_code = works_pb2.ERR_NONE
    auth_resp.base_response.err_str = 'good luck'
    auth_resp.uin = 100000
    auth_resp.session_key = 'hello'

    resp_buf = pack_utils.encode(
        buf=auth_resp.SerializeToString(),
        cookie='',
        encrypt=Packet.CRYPT_NONE,
        key='password')
    return resp_buf


def application(env, start_response):
    req_buf = read_buf.init(env)
    resp_buf = process(req_buf)
    return read_buf.finish(start_response, resp_buf)







