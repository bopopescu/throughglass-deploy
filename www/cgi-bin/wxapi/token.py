# -*- coding: UTF-8 -*-

import os
import pickle
import urllib2
import json
import datetime
import time
import logging

from model import config
import errors


def load_token():
    if os.path.isfile('record/access_token.txt'):
        file_handle = open('record/access_token.txt', 'rb')
        # token_info = ['', 7200, 0]
        token_info = pickle.load(file_handle)
        file_handle.close()
        return token_info

    else:
        return ['', 7200, 0]


def update_token():
    logging.debug('access token file: %s' % os.path.abspath('record/access_token.txt'))

    url = 'https://api.weixin.qq.com/cgi-bin/token' \
          '?grant_type=client_credential' \
          '&appid=%s' \
          '&secret=%s' \
          % (config.wxapi_config.get('app_id'), config.wxapi_config.get('app_secret'))
    # print url

    contents = urllib2.urlopen(url).read()
    # print contents
    python_object = json.loads(contents)
    token_info = [
        python_object.get('access_token'),
        python_object.get('expires_in'),
        time.mktime(datetime.datetime.now().timetuple())
    ]

    file_handle = open('record/access_token.txt', 'w')
    pickle.dump(token_info, file_handle)
    file_handle.close()

    # print token_info
    return token_info


# get token: get from local first
def get_token():
    token_info = load_token()

    check_time = time.mktime(datetime.datetime.now().timetuple()) - token_info[2]

    if token_info[1] < check_time:
        token_info = update_token()
        logging.debug('update token from wechat, checktime = %d' % check_time)

    else:
        logging.debug('loading token from cache, checktime = %d' % check_time)

    return token_info[0]


def refresh_user_token(refresh_token):
    refresh_url = (
        "https://api.weixin.qq.com/sns/oauth2/refresh_token?grant_type=refresh_token&appid=%s&refresh_token=%s"
        % (config.wxapi_config.get('app_id'),
           refresh_token))

    # "access_token":"ACCESS_TOKEN",
    # "expires_in":7200,
    # "refresh_token":"REFRESH_TOKEN",
    # "openid":"OPENID",
    # "scope":"SCOPE"
    err_code, err_str, extra = errors.parse_error(urllib2.urlopen(refresh_url).read())
    logging.debug('refresh access token, url = %s, err = %d' % (refresh_url, err_code))
    return err_code, err_str, extra


def authorize_code(code):
    # access token
    url = ('https://api.weixin.qq.com/sns/oauth2/access_token?appid=%s&secret=%s&code=%s&grant_type=authorization_code'
           % (config.wxapi_config.get('app_id'),
              config.wxapi_config.get('app_secret'),
              code))

    err_code, err_str, j = errors.parse_error(urllib2.urlopen(url).read())

    # user info
    url = ('https://api.weixin.qq.com/sns/userinfo?access_token=%s&openid=%s'
           % (j.get('access_token'),
              j.get('openid')))

    err_code, err_str, j2 = errors.parse_error(urllib2.urlopen(url).read())

    # update user_token
    wx = {
        'openid': j.get('openid'),
        'access_token': j.get('access_token'),
        'refresh_token': j.get('refresh_token'),
        'expires_in': j.get('expires_in'),
        'display': j2.get('nickname')
    }

    return wx
