import base64
import logging
import os
import uuid

import tornado.httpserver
import tornado.ioloop
import tornado.options
from core.AntiTamper import AntiTamper
from handlers.ConfigHandler import ConfigHandler
from handlers.FileEventHandler import FileEventHandler
from handlers.FileEventsHandler import FileEventsHandler
from handlers.IndexHandler import IndexHandler
from tornado.options import define

from db_manager.sqlite.SQLiteDBManager import SQLiteDBManager
from db_manager.sqlite.models import init_db


def getHandlers(app):
    return [
        (r"/", IndexHandler),

        (r"/config", ConfigHandler),

        (r"/file_event/([0-9]+)", FileEventHandler),
        (r"/file_events", FileEventsHandler)
    ]



define("port", default=8000, help="run on the given port", type=int)
define("debug", default=False, help="run on debug mode", type=bool)

class Server():
    settings = {
        "cookie_secret": "bZJc2sWbQLKos6GkHn/VB9oXwQt8S0R0kRvJ5/xJ89E=",
        "xsrf_cookies": False
    }

    def __init__(self):
        self.log = None

    def start(self, port=8000):
        self.log.info("zywaf_at_module is starting...")
        self.handlers = getHandlers(self)

        secret_key = base64.b64encode(uuid.uuid4().bytes + uuid.uuid4().bytes)
        settings = {
            "cookie_secret": secret_key,
            "xsrf_cookies": False
        }
        app = tornado.web.Application(handlers=self.handlers, **settings)

        #db_path = os.path.dirname(os.path.abspath(__file__)) + '/data/at.db'
        db_path = './data/at.db'
        sqlite_db = init_db(db_path)
        self.db_mgr = SQLiteDBManager(sqlite_db)
        self.log.info("db location: %s" % db_path)

        app.server = self
        server = tornado.httpserver.HTTPServer(app)
        server.listen(port)

        self.webserver = server
        self.log.info("debug mode: %s" % self.is_debug)
        self.log.info("listen to port: %s" % port)

        # add daily task here
        #daily_task = tornado.ioloop.PeriodicCallback(daily_refresh, 10 * 1000)
        #daily_task.start()

        # start file system monitor here
        # path = sys.argv[1] if len(sys.argv) > 1 else '.'  # get monitored path
        path = '/Users/ywang/workspace/python/pycharm/zyWAF_AT_test/doc'
        self.at = AntiTamper(path, self.db_mgr)
        self.at.monitor_on()

        tornado.ioloop.IOLoop.instance().start()



if __name__ == "__main__":
    tornado.options.parse_command_line()
    options = tornado.options.options

    server = Server()
    server.is_debug = options.debug
    server.log = logging.getLogger("zywaf_at")
    server.start(options.port)




