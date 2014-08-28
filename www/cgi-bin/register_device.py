#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = 'guang_hik'
import cgitb

cgitb.enable()

import sys
import logging
import hashlib
import time

import mysql.connector
import model.config
from ye2pack.works_pb2 import RegisterDevice
from ye2pack import pack_utils, works_pb2
from ye2pack.pack_pb2 import Packet


def generate_username(device_id):
    user = 'auto_' + hashlib.md5(device_id).hexdigest()
    return user


def generate_session():
    return time.time()


private_key = ''

req_buf = sys.stdin.read()
req_pkt = pack_utils.decode(req_buf, private_key)

# register device
req = RegisterDevice.Request()
req.ParseFromString(req_pkt.data)

device_id = req.device_id

# generate username
username = generate_username(device_id)
session = generate_session()

logging.debug("register device=%s, username=%s, session=%s", (req.device_id, username, session))

#
cnx = mysql.connector.connect(**model.config.rw_config)
cursor = cnx.cursor()

sql_pattern = ("REPLACE INTO userinfo "
               "(device_id, username, session) "
               "VALUES (%(device_id)s, %(username)s, %(session)s) ")

sql_value = {
    'device_id': device_id,
    'username': username,
    'session': session
}

cursor.execute(sql_pattern, sql_value)
uin = cursor.lastrowid
cnx.commit()

cursor.close()
cnx.close()


# write response
resp = RegisterDevice.Response()
resp.base_response.err_code = works_pb2.ERR_NONE
resp.username = username
resp.uin = uin

# resp_buf = pack_utils.encode(buf=resp.SerializeToString(), encrypt=Packet.CRYPT_RSA, key=private_key)
resp_buf = pack_utils.encode(buf=resp.SerializeToString(), encrypt=Packet.CRYPT_NONE, key=private_key, uin=uin)

print "Content-Type: text/plain;charset=utf-8"
print

print resp_buf