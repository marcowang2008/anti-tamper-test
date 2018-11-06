import logging
import sys
import threading
import time

from core.logging_handlers.SQLiteLoggingEventHandler import SQLiteLoggingEventHandler
from watchdog.observers import Observer

class AntiTamper(object):
    def __init__(self, path, db):
        self.path = path
        self.db = db
        self.observer = Observer()


    def monitor_off(self):
        print("=====monitor_off")
        self.observer.stop()
        self.observer.join()


    def monitor_on(self):
        print("=====monitor_on: %s" % self.path)
        t = threading.Thread(target=self.do_monitor)
        t.start()


    def do_monitor(self):
        print("=====do_monitor")
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s - %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S')
        event_handler = SQLiteLoggingEventHandler(self.db)
        self.observer.schedule(event_handler, self.path, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.observer.stop()
        self.observer.join()



