# -*- coding: UTF-8 -*-

import logging

from ye2pack import pack_utils, works_pb2
from ye2pack.works_pb2 import Post
from ye2pack.pack_pb2 import Packet
from model import usr_info, bind_accounts
from wxapi import errors, timeline


def process(req_buf):
    req_pkt = pack_utils.pre_decode(buf=req_buf)
    uin = req_pkt.uin

    usr = usr_info.query(uin)
    session = usr.get('session')

    req_pkt = pack_utils.decode(req_buf, '')
    req = Post.Request()
    req.ParseFromString(req_pkt.data)

    # TODO:
    access_token = bind_accounts.query_access_token(
        uin=req.base_request.uin,
        account_type='weixin.qq.com'
    )

    err_code, err_str, extra = timeline.post_multi(access_token, req.media_id, req.comment)
    logging.debug("try timeline post err = %d, %s" % (err_code, err_str))

    # construct post response
    resp = Post.Response()
    resp.id = 0

    if err_code == errors.ERR_NONE:
        resp.base_response.err_code = works_pb2.ERR_NONE
        resp.base_response.err_str = 'good luck'

    elif err_code == errors.ERR_ACCESS_TOKEN_EXPIRED:
        # access token expired, renew it
        resp.base_response.err_code, resp.base_response.err_str = bind_accounts.renew_access_token(uin)
        if resp.base_response.err_code == errors.ERR_NONE:
            access_token = bind_accounts.query_access_token(
                uin=req.base_request.uin,
                account_type='weixin.qq.com'
            )
            logging.debug("renewed user access token, %s" % access_token)

            # post again
            resp.base_response.err_code, resp.base_response.err_str, extra = timeline.post_multi(
                access_token, req.media_id, req.comment)

        else:
            # renew failed
            logging.debug("renewed user access token failed, err = %d, %s"
                          % (resp.base_response.err_code,
                             resp.base_response.err_str))

    else:
        resp.base_response.err_code = err_code
        resp.base_response.err_str = err_str

    resp_buf = pack_utils.encode(
        buf=resp.SerializeToString(),
        encrypt=Packet.CRYPT_NONE,
        key=session)

    return resp_buf