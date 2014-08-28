#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = 'yowenlove'

import mysql.connector
import config
import hashlib


def update(uin, openid, access_token, refresh_token, expires_in, account_type='weixin.qq.com', display='', extra=''):
    cnx = mysql.connector.connect(**config.ro_config)
    cursor = cnx.cursor()

    bind_hash = hashlib.md5('u=%d,d=%s' % (uin, account_type)).hexdigest()

    sql_pattern = (
        "REPLACE INTO bindaccount SET "
        "bind_hash = %(bind_hash)s, "
        "uid = %(uid)s, "
        "openid = %(openid)s, "
        "type = %(type)s, "
        "display = %(display)s, "
        "access_token = %(access_token)s, "
        "refresh_token = %(refresh_token)s, "
        "expires_in = %(expires_in)s, "
        "extra = %(extra)s "
    )

    sql_value = {
        'bind_hash': bind_hash,
        'openid': openid,
        'uid': uin,
        'type': account_type,
        'display': display,
        'access_token': access_token,
        'refresh_token': refresh_token,
        'expires_in': expires_in,
        'extra': extra
    }

    cursor.execute(sql_pattern, sql_value)
    cnx.commit()

    cursor.close()
    cnx.close()

    return


def query_access_token(uin, account_type):
    cnx = mysql.connector.connect(**config.ro_config)
    cursor = cnx.cursor()

    bind_hash = hashlib.md5('u=%d,d=%s' % (uin, account_type)).hexdigest()

    print bind_hash

    sql_pattern = (
        "SELECT access_token FROM bindaccount "
        "WHERE bind_hash = %(bind_hash)s"
    )

    sql_value = {
        'bind_hash': bind_hash
    }

    cursor.execute(sql_pattern, sql_value)
    data = cursor.fetchone()

    cnx.commit()

    cursor.close()
    cnx.close()
    return data[0]