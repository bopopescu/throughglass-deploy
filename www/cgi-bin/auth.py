# -*- coding: UTF-8 -*-

# enable debugging

from ye2pack import pack_utils, works_pb2
from ye2pack.works_pb2 import Auth
from ye2pack.pack_pb2 import Packet
import rsa


def application(env, start_response):

	response_headers = [
		('Content-type', 'text/plain')
	]

	start_response('200 OK', response_headers)

	private_key = rsa.PrivateKey(
		11176276734117980437, 65537, 6939363295624337393, 12879322847, 867768971)

	req_pkt = pack_utils.decode(buf=req_buf, key=private_key)
	auth_req = Auth.Request()
	auth_req.ParseFromString(req_pkt.data)

	# print('request username = %s, password = %s' % (auth_req.username, auth_req.password))

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

	yield resp_buf







