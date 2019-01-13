import logging
import tornado.ioloop
from tornado.options import define, options, parse_command_line
import threading
import time

from application import Application

define("port", default=8000, help="run on the given port", type=int)

def start_tornado(*args, **kwargs):
    options.parse_command_line()
    app = Application()
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()

def stop_tornado():
    ioloop = tornado.ioloop.IOLoop.instance()
    ioloop.add_callback(ioloop.stop)
    print("Asked Tornado to exit")

def main():
    t = threading.Thread(target=start_tornado)
    t.start()
    time.sleep(20)
    stop_tornado()
    t.join()

if __name__ == "__main__":
    main()
