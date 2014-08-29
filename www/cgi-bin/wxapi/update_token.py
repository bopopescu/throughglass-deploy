#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# enable debugging
import os
import pickle
import urllib2
import json
import datetime
import time

from model import config


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
    # print config.wxapi_config

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

    if token_info[2] < check_time:
        token_info = update_token()

    return token_info[0]


def update_user_token(code):
    # access token
    url = ('https://api.weixin.qq.com/sns/oauth2/access_token?appid=%s&secret=%s&code=%s&grant_type=authorization_code'
           % (config.wxapi_config.get('app_id'),
              config.wxapi_config.get('app_secret'),
              code))

    http_request = urllib2.Request(url)
    http_response = urllib2.urlopen(http_request)
    result = http_response.read()

    j = json.loads(result)

    # user info
    url = ('https://api.weixin.qq.com/sns/userinfo?access_token=%s&openid=%s'
           % (j.get('access_token'),
              j.get('openid')))

    http_request = urllib2.Request(url)
    http_response = urllib2.urlopen(http_request)
    result = http_response.read()
    j2 = json.loads(result)

    # update user_token
    wx = {
        'openid': j.get('openid'),
        'access_token': j.get('access_token'),
        'refresh_token': j.get('refresh_token'),
        'expires_in': j.get('expires_in'),
        'display': j2.get('nickname')
    }

    return wx


def __test__update_user_token(code):
    openid = u'on2p6jt8airA1_fpby9K1ToohkEc'
    access_token = u'OezXcEiiBSKSxW0eoylIePSAYgNWJaCIBO67zda4qeQjcS_5...anYrlCy-ak-xi-1OqzRbQsW2Ml4Oa-tuXgnZW0kUwo9z2yUhg'
    refresh_token = u'OezXcEiiBSKSxW0eoylIePSAYgNWJaCIBO67zda4qeQjcS_5...8l74tMsKQZJz8C7VBToFIJ0UzdDptP7cxduS8sq0ioN_6kUzf'
    expires_in = 7200
    account_type = 'weixin.qq.com'
    display = u'\u8fdc\u5149'
    extra = ''

    wx = {
        'openid': openid,
        'access_token': access_token,
        'refresh_token': refresh_token,
        'expires_in': expires_in,
        'display': display
    }
    return wx