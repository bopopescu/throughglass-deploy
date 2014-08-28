# -*- coding: UTF-8 -*-

# from config_online import ro_user, ro_pass, rw_user, rw_pass, hostname, database
from config_localhost import ro_user, ro_pass, rw_user, rw_pass, hostname, database

__author__ = 'guang_hik'

ro_config = {
    'user': ro_user,
    'password': ro_pass,
    'host': hostname,
    'database': database,
    'unix_socket': '/opt/local/var/run/mysql51/mysqld.sock'
}

rw_config = {
    'user': rw_user,
    'password': rw_pass,
    'host': hostname,
    'database': database,
    'unix_socket': '/opt/local/var/run/mysql51/mysqld.sock'
}

wxapi_config = {
    'app_id' : 'wx05234d30bff5a7da',
    'app_secret' : '18c76b9dda313b4e613f1358a9eaf495',
}