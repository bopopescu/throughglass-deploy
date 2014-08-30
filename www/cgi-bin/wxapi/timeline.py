# -*- coding: UTF-8 -*-

import urllib2
import errors


def post_multi(access_token, media_id, comment=''):
    url = ('http://api.weixin.qq.com/sns/timeline/multi?access_token=%s' % access_token)

    media_set = ('{"media_id":"%s"}' % media_id[0])
    for i in media_id[1:]:
        media_set = media_set + (', {"media_id":"%s"}' % i)

    values = ('{"type":"image", "description":"%s", "image_list": [%s]' % (comment, media_set))

    http_request = urllib2.Request(url, values)
    err_code, err_str, extra = errors.parse_error(urllib2.urlopen(http_request).read())
    return err_code, err_str, extra