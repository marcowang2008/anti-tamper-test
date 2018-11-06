import logging
from datetime import datetime

from core.logging_handlers._BaseLoggingEventHandler import BaseLoggingEventHandler


class SQLiteLoggingEventHandler(BaseLoggingEventHandler):
    db = None

    """Logs all the events captured into SQLite db"""
    def __init__(self, db):
        self.db = db


    def log_event(self, event, behave):
        type = 'directory' if event.is_directory else 'file'
        self.db.create_file_event(behave, event.src_path, datetime.now(), type)


    def on_moved(self, event):
        #super(MyLoggingEventHandler, self).on_moved(event)
        self.log_event(event, 'moved')
        what = 'directory' if event.is_directory else 'file'
        print("Moved %s: from %s to %s", what, event.src_path, event.dest_path)


    def on_created(self, event):
        #super(MyLoggingEventHandler, self).on_created(event)
        self.log_event(event, 'created')
        what = 'directory' if event.is_directory else 'file'
        print("Created %s: %s", what, event.src_path)


    def on_deleted(self, event):
        #super(MyLoggingEventHandler, self).on_deleted(event)
        self.log_event(event, 'deleted')
        what = 'directory' if event.is_directory else 'file'
        print("Deleted %s: %s", what, event.src_path)


    def on_modified(self, event):
        #super(MyLoggingEventHandler, self).on_modified(event)
        self.log_event(event, 'modified')
        what = 'directory' if event.is_directory else 'file'
        print("Modified %s: %s", what, event.src_path)