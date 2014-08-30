# -*- coding: UTF-8 -*-

import urllib2

from ye2pack import pack_utils, works_pb2
from ye2pack.works_pb2 import Post
from ye2pack.pack_pb2 import Packet
from model import usr_info, bind_accounts
from wxapi import errors


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

    url = ('http://api.weixin.qq.com/sns/timeline/multi?access_token=%s' % access_token)

    media_set = ('{"media_id":"%s"}' % req.media_id[0])
    for i in req.media_id[1:]:
        media_set = media_set + (', {"media_id":"%s"}' % i)

    values = ('{"type":"image", "description":"%s", "image_list": [%s]' % (req.comment, media_set))

    http_request = urllib2.Request(url, values)
    http_response = urllib2.urlopen(http_request)
    result = http_response.read()
    err_code, err_str = errors.parse_error(result)

    # construct post response
    resp = Post.Response()
    resp.id = 0

    if err_code == errors.ERR_NONE:
        resp.base_response.err_code = works_pb2.ERR_NONE
        resp.base_response.err_str = 'good luck'

    elif err_code == errors.ERR_ACCESS_TOKEN_EXPIRED:
        bind_accounts.renew_access_token(uin)
        resp.base_response.err_code, resp.base_response.err_str = errors.parse_error(urllib2.urlopen(url).read())

    else:
        resp.base_response.err_code = err_code
        resp.base_response.err_str = err_str

    resp_buf = pack_utils.encode(
        buf=resp.SerializeToString(),
        encrypt=Packet.CRYPT_NONE,
        key=session)

    return resp_buf