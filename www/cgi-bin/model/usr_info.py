#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = 'yowenlove'

import mysql.connector
import config


def query(uin):
    # print "uid=%d" % uin

    cnx = mysql.connector.connect(**config.ro_config)

    cursor = cnx.cursor()

    sql_pattern = (
        "SELECT session FROM userinfo "
        "WHERE uid = %(uid)s"
    )

    sql_value = {
        'uid': uin
    }

    cursor.execute(sql_pattern, sql_value)
    data = cursor.fetchone()

    usr = {
        'session': data[0]
    }

    cursor.close()
    cnx.close()

    return usr