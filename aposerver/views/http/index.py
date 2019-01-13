import tornado.web
import json

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        print("In main handler")
        self.write(json.dumps({'hello':'world'}))