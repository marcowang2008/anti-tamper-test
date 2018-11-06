import os
import sys
from sqlalchemy import (
    String,
    Column,
    Integer,
    Boolean,
    DateTime,
    ForeignKey,
    Text,
    types,
    VARCHAR
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from datetime import datetime


Base = declarative_base()


class FileEvent(Base):
    __tablename__ = 'file_event'
    __table_args__ = {'sqlite_autoincrement': True}

    id = Column(Integer, primary_key=True)
    event = Column(String(16)) # modify/delete/create
    path = Column(Text)
    type = Column(String(16))   # file or folder
    event_time = Column(DateTime)   # when this file event happens
    is_handled = Column(Boolean, default=False)
    is_ignored = Column(Boolean, default=False)
    reason = Column(String(32))
    created = Column(DateTime, default=datetime.now)    # when this record is created
    modified = Column(DateTime)

    def _public_props(self):
        ret = {}
        ret['id'] = self.id
        ret['event'] = self.event
        ret['path'] = self.path
        ret['type'] = self.type
        ret['event_time'] = self.event_time.strftime("%Y-%m-%d %H:%M:%S")
        ret['is_handled'] = self.is_handled
        ret['is_ignored'] = self.is_ignored
        ret['reason'] = self.reason if self.reason  else None
        ret['created'] = self.created.strftime("%Y-%m-%d %H:%M:%S")
        ret['modified'] = self.modified.strftime("%Y-%m-%d %H:%M:%S") if self.modified else None
        return ret



class FileEventHandleLog(Base):
    __tablename__ = 'file_event_handle_log'
    __table_args__ = {'sqlite_autoincrement': True}

    id = Column(Integer, primary_key=True)
    file_event_id = Column(Integer, ForeignKey('file_event.id')) # one-to-many
    action = Column(String(16)) # user defined allowed action
    operator = Column(String(16))  # who made this action, admin or AT_policy?
    created = Column(DateTime, default=datetime.now)

    file_event = relationship('FileEvent', backref=backref('file_event', order_by=id))

    def _public_props(self):
        ret = {}
        ret['id'] = self.id
        ret['action'] = self.action
        ret['operator'] = self.operator
        ret['created'] = self.created.strftime("%Y-%m-%d %H:%M:%S")
        ret['file_event'] = self.file_event._public_props()
        return ret



def init_db(db_path):
    # create sqlite engine
    engine = create_engine("sqlite:///" + db_path)
    # create tables
    Base.metadata.create_all(bind=engine)
    return scoped_session(sessionmaker(bind=engine))