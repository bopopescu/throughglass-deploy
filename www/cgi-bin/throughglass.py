# -*- coding: UTF-8 -*-

import web

import auth
import get_wechat_upload_token
import post
import update_wechat_account
import logging

urls = (
    '/cgi-bin/auth.py', 'AuthHandler',
    '/cgi-bin/update_wechat_account.py', 'UpdateWeChatAccountHandler',
    '/cgi-bin/post.py', 'PostHandler',
    '/cgi-bin/get_wechat_upload_token.py', 'GetWeChatUploadTokenHandler',
)

app = web.application(urls, globals())

logging.basicConfig(level=logging.DEBUG)

class AuthHandler:
    def __init__(self):
        return

    def POST(self):
        # web.header('Content-Type', 'text/plain')
        return auth.process(web.data())

    def GET(self):
        # web.header('Content-Type', 'text/plain')
        return auth.process(web.data())


class UpdateWeChatAccountHandler:
    def __init__(self):
        return

    def POST(self):
        # web.header('Content-Type', 'text/plain')
        return update_wechat_account.process(web.data())

    def GET(self):
        # web.header('Content-Type', 'text/plain')
        return update_wechat_account.process(web.data())


class PostHandler:
    def __init__(self):
        return

    def POST(self):
        # web.header('Content-Type', 'text/plain')
        return post.process(web.data())

    def GET(self):
        # web.header('Content-Type', 'text/plain')
        return post.process(web.data())


class GetWeChatUploadTokenHandler:
    def __init__(self):
        return

    def POST(self):
        # web.header('Content-Type', 'text/plain')
        return get_wechat_upload_token.process(web.data())

    def GET(self):
        # web.header('Content-Type', 'text/plain')
        return get_wechat_upload_token.process(web.data())


application = app.wsgifunc()
