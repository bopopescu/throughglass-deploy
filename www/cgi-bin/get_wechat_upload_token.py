# -*- coding: UTF-8 -*-


from ye2pack import pack_utils, works_pb2
from ye2pack.pack_pb2 import Packet
from ye2pack.works_pb2 import GetWeChatUploadToken
from model import usr_info
from wxapi import update_token


def process(req_buf):
    req_pkt = pack_utils.pre_decode(buf=req_buf)
    uin = req_pkt.uin

    usr = usr_info.query(uin)
    session = usr.get('session')

    req_pkt = pack_utils.decode(buf=req_buf, key=session)
    req = GetWeChatUploadToken.Request()
    req.ParseFromString(req_pkt.data)

    resp = GetWeChatUploadToken.Response()
    resp.base_response.err_code = works_pb2.ERR_NONE
    resp.token = update_token.get_token()

    resp_buf = pack_utils.encode(
        buf=resp.SerializeToString(),
        encrypt=Packet.CRYPT_NONE,
        key=session,
        uin=uin
    )
    return resp_buf
