# -*- coding: UTF-8 -*-

import web

import auth
import update_wechat_account

urls = (
    '/cgi-bin/auth.py', 'AuthHandler',
    '/cgi-bin/update_wechat_account.py', 'UpdateWeChatAccountHandler',
)

app = web.application(urls, globals())


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


application = app.wsgifunc()
