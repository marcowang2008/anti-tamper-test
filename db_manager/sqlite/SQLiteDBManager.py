from db_manager._BaseDBManager import BaseDBManager
from db_manager.sqlite.models import FileEvent

class SQLiteDBManager(BaseDBManager):
    def __init__(self, db):
        self.db = db

    def read_file_event_by_id(self, id):
        fevent = self.db.query(FileEvent).filter_by(id=id).one()
        return fevent._public_props()


    def update_file_event(self, file_event):
        fevent = self.db.query(FileEvent).filter_by(id=file_event['id']).one()
        fevent.is_handled = file_event['is_handled']
        fevent.is_ignored = file_event['is_ignored']
        self.db.commit()
        return fevent._public_props()


    def read_file_events_by_page(self, page=0, row_per_page=20):
        fevents = self.db.query(FileEvent).limit(row_per_page).offset(page*row_per_page).all()
        return [f._public_props() for f in fevents]


    def create_file_event(self, behave, path, event_time, type):
        new_fevent = FileEvent(event=behave,
                               path=path,
                               event_time=event_time,
                               type=type)
        self.db.add(new_fevent)
        self.db.commit()







