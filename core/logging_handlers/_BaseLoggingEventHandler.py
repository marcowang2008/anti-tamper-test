from watchdog.events import LoggingEventHandler


class BaseLoggingEventHandler(LoggingEventHandler):
    """Logs all the events captured."""
    @property
    def db(self):
        return self.application.server.db

    def on_moved(self, event):
        super(BaseLoggingEventHandler, self).on_moved(event)

    def on_created(self, event):
        super(BaseLoggingEventHandler, self).on_created(event)

    def on_deleted(self, event):
        super(BaseLoggingEventHandler, self).on_deleted(event)

    def on_modified(self, event):
        super(BaseLoggingEventHandler, self).on_modified(event)