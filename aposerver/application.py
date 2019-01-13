import tornado.web

from views.http import HTTP_HANDLERS
from views.websockets import SOCKET_HANDLERS

import os

class Application(tornado.web.Application):
    def __init__(self):
        handlers = list()
        handlers.extend(HTTP_HANDLERS)
        handlers.extend(SOCKET_HANDLERS)

        settings = dict(
            cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            xsrf_cookies=True,
        )
        super().__init__(handlers, **settings)