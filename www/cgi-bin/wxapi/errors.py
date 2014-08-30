# -*- coding: UTF-8 -*-

import json

# errors define
ERR_NONE = 0

ERR_INVALID_CREDENTIAL = 40001  # invalid credential	不合法的调用凭证
ERR_INVALID_GRANT_TYPE = 40002  # invalid grant_type	不合法的grant_type
ERR_INVALID_OPENID = 40003  # invalid openid	不合法的OpenID
ERR_INVALID_MEDIA_TYPE = 40004  # invalid media type	不合法的媒体文件类型
ERR_INVALID_MEDIA_ID = 40007  # invalid media_id	不合法的media_id
ERR_INVALID_MESSAGE_TYPE = 40008  # invalid message type	不合法的message_type
ERR_INVALID_IMAGE_SIZE = 40009  # invalid image size	不合法的图片大小
ERR_INVALID_VOICE_SIZE = 40010  # invalid voice size	不合法的语音大小
ERR_INVALID_VIDEO_SIZE = 40011  # invalid video size	不合法的视频大小
ERR_INVALID_THUMB_SIZE = 40012  # invalid thumb size	不合法的缩略图大小
ERR_INVALID_APPID = 40013  # invalid appid	不合法的AppID
ERR_INVALID_ACCESS_TOKEN = 40014  # invalid access_token	不合法的access_token
ERR_INVALID_MENU_TYPE = 40015  # invalid menu type	不合法的菜单类型
ERR_INVALID_BUTTON_SIZE = 40016  # invalid button size	不合法的菜单按钮个数
ERR_INVALID_BUTTON_TYPE = 40017  # invalid button type	不合法的按钮类型
ERR_INVALID_BUTTON_NAME_SIZE = 40018  # invalid button name size	不合法的按钮名称长度
ERR_INVALID_BUTTON_KEY_SIZE = 40019  # invalid button key size	不合法的按钮KEY长度
ERR_INVALID_BUTTON_URL_SIZE = 40020  # invalid button url size	不合法的url长度
ERR_INVALID_SUB_BUTTON_SIZE = 40023  # invalid sub button size	不合法的子菜单按钮个数
ERR_INVALID_SUB_BUTTON_TYPE = 40024  # invalid sub button type	不合法的子菜单类型
ERR_INVALID_SUB_BUTTON_NAME_SIZE = 40025  # invalid sub button name size	不合法的子菜单按钮名称长度
ERR_INVALID_SUB_BUTTON_KEY_SIZE = 40026  # invalid sub button key size	不合法的子菜单按钮KEY长度
ERR_INVALID_SUB_BUTTON_URL_SIZE = 40027  # invalid sub button url size	不合法的子菜单按钮url长度
ERR_INVALID_CODE = 40029  # invalid code	不合法或已过期的code
ERR_INVALID_REFRESH_TOKEN = 40030  # invalid refresh_token	不合法的refresh_token
ERR_INVALID_TEMPLATE_ID_SIZE = 40036  # invalid template_id size	不合法的template_id长度
ERR_INVALID_TEMPLATE_ID = 40037  # invalid template_id	不合法的template_id
ERR_INVALID_URL_SIZE = 40039  # invalid url size	不合法的url长度
ERR_INVALID_URL_DOMAIN = 40048  # invalid url domain	不合法的url域名
ERR_INVALID_SUB_BUTTON_URL_DOMAIN = 40054  # invalid sub button url domain	不合法的子菜单按钮url域名
ERR_INVALID_BUTTON_URL_DOMAIN = 40055  # invalid button url domain	不合法的菜单按钮url域名
ERR_INVALID_URL = 40066  # invalid url	不合法的url
ERR_ACCESS_TOKEN_MISSING = 41001  # access_token missing	缺失access_token参数
ERR_APPID_MISSING = 41002  # appid missing	缺失appid参数
ERR_REFRESH_TOKEN_MISSING = 41003  # refresh_token missing	缺失refresh_token参数
ERR_APPSECRET_MISSING = 41004  # appsecret missing	缺失secret参数
ERR_MEDIA_DATA_MISSING = 41005  # media data missing	缺失二进制媒体文件
ERR_MEDIA_ID_MISSING = 41006  # media_id missing	缺失media_id参数
ERR_SUB_MENU_DATA_MISSING = 41007  # sub_menu data missing	缺失子菜单数据
ERR_MISSING_CODE = 41008  # missing code	缺失code参数
ERR_MISSING_OPENID = 41009  # missing openid	缺失openid参数
ERR_MISSING_URL = 41010  # missing url	缺失url参数
ERR_ACCESS_TOKEN_EXPIRED = 42001  # access_token expired	access_token超时
ERR_REFRESH_TOKEN_EXPIRED = 42002  # refresh_token expired	refresh_token超时
ERR_CODE_EXPIRED = 42003  # code expired	code超时
ERR_REQUIRE_GET_METHOD = 43001  # require GET method	需要使用GET方法请求
ERR_REQUIRE_POST_METHOD = 43002  # require POST method	需要使用POST方法请求
ERR_REQUIRE_HTTPS = 43003  # require https	需要使用HTTPS
ERR_REQUIRE_SUBSCRIBE = 43004  # require subscribe	需要订阅关系
ERR_EMPTY_MEDIA_DATA = 44001  # empty media data	空白的二进制数据
ERR_EMPTY_POST_DATA = 44002  # empty post data	空白的POST数据
ERR_EMPTY_NEWS_DATA = 44003  # empty news data	空白的news数据
ERR_EMPTY_CONTENT = 44004  # empty content	空白的内容
ERR_EMPTY_LIST_SIZE = 44005  # empty list size	空白的列表
ERR_MEDIA_SIZE_OUT_OF_LIMIT = 45001  # media size out of limit	二进制文件超过限制
ERR_CONTENT_SIZE_OUT_OF_LIMIT = 45002  # content size out of limit	content参数超过限制
ERR_TITLE_SIZE_OUT_OF_LIMIT = 45003  # title size out of limit	title参数超过限制
ERR_DESCRIPTION_SIZE_OUT_OF_LIMIT = 45004  # description size out of limit	description参数超过限制
ERR_URL_SIZE_OUT_OF_LIMIT = 45005  # url size out of limit	url参数长度超过限制
ERR_PICURL_SIZE_OUT_OF_LIMIT = 45006  # picurl size out of limit	picurl参数超过限制
ERR_PLAYTIME_OUT_OF_LIMIT = 45007  # playtime out of limit	播放时间超过限制（语音为60s最大）
ERR_ARTICLE_SIZE_OUT_OF_LIMIT = 45008  # article size out of limit	article参数超过限制
ERR_API_FREQ_OUT_OF_LIMIT = 45009  # api freq out of limit	接口调动频率超过限制
ERR_CREATE_MENU_LIMIT = 45010  # create menu limit	建立菜单被限制
ERR_API_LIMIT = 45011  # api limit	频率限制
ERR_TEMPLATE_SIZE_OUT_OF_LIMIT = 45012  # template size out of limit	模板大小超过限制
ERR_CANNOT_MODIFY_SYS_GROUP = 45016  # can't modify sys group	不能修改默认组
ERR_GROUP_NAME_TOO_LONG = 45017  # can't set group name too long sys group	修改组名过长
ERR_TOO_MANY_GROUP_NOW = 45018  # too many group now, no need to add new	组数量过多
ERR_API_UNAUTHORIZED = 50001  # api unauthorized	接口未授权


def parse_error(result):
    j = json.loads(result)
    err_code = j.get('errcode')
    err_str = j.get('errmsg')
    return err_code, err_str