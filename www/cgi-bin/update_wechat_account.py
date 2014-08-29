# -*- coding: UTF-8 -*-


from ye2pack import pack_utils, works_pb2
from ye2pack.pack_pb2 import Packet
from ye2pack.works_pb2 import UpdateWeChatAccount
from model import usr_info, bind_accounts
from wxapi import update_token

import read_buf
import logging


def process(req_buf):
    req_pkt = pack_utils.pre_decode(buf=req_buf)
    uin = req_pkt.uin

    usr = usr_info.query(uin)
    session = usr.get('session')
    logging.info('session=%s, uin=%d' % (session, uin))

    req_pkt = pack_utils.decode(buf=req_buf, key=session)
    req = UpdateWeChatAccount.Request()
    req.ParseFromString(req_pkt.data)

    # update from wechat server
    _info = update_token.update_user_token(req.code)
    # _info = update_token.__test__update_user_token(req.code)

    # prepare for return
    resp = UpdateWeChatAccount.Response()
    resp.bind_account.openid = _info.get('openid')
    resp.bind_account.type = 'weixin.qq.com'
    resp.bind_account.access_token = _info.get('access_token')
    resp.bind_account.refresh_token = _info.get('refresh_token')
    resp.bind_account.expires_in = _info.get('expires_in')
    resp.bind_account.display = _info.get('display')

    # update server side record
    bind_accounts.update(
        uin=req.base_request.uin,
        openid=resp.bind_account.openid,
        account_type=resp.bind_account.type,
        access_token=resp.bind_account.access_token,
        refresh_token=resp.bind_account.refresh_token,
        expires_in=resp.bind_account.expires_in,
        display=resp.bind_account.display
    )

    resp.base_response.err_code = works_pb2.ERR_NONE
    resp_buf = pack_utils.encode(
        buf=resp.SerializeToString(),
        encrypt=Packet.CRYPT_NONE,
        key=session,
        uin=req_pkt.uin
    )
    return resp_buf


def application(env, start_response):
    req_buf = read_buf.init(env)
    resp_buf = process(req_buf)
    return read_buf.finish(start_response, resp_buf)