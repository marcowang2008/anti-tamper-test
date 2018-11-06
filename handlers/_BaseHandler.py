import tornado.web
import errors
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
from sqlalchemy.exc import IntegrityError


class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        return self.application.server.db_mgr


    def initialize(self):
        self.log = self.application.server.log


    def prepare(self):
        try:
            # do validation here
            pass
        except Exception as e:
            self.finish()


    def format_api_return(self, data=None, error=None, msg=None):
        if data:
            # make sure all return with an error code even there is no error
            # data['ecode'] = errors.NO_ERROR['ecode']
            return data
        else:
            # data is None and there is an error
            if msg: error['info'] = msg
            return error


    def handle_db_error_msg(self, e):
        if type(e) is NoResultFound:    # thrown by sqlalchemy one()
            return errors.DB_NO_RESULT
        elif type(e) is MultipleResultsFound:   # thrown by sqlalchemy one()
            return errors.DB_MORE_THAN_ONE_RESULT
        elif type(e) is IntegrityError: # transaction failed! we need to rollback, pal!
            self.db.rollback()
            return errors.DB_TRANSACTION_FAILED
        elif type(e) is errors.MissingParamException:
            return errors.REQ_MISSING_PARAM
        else:
            return errors.UNDEFINED_ERROR
