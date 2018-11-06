import errors
import tornado.web
from handlers._BaseHandler import BaseHandler


class FileEventHandler(BaseHandler):

    def get_params(self):
        """
        get parampeters and check if all key parameter is available
        """
        jdata = tornado.escape.json_decode(self.request.body)
        if ('is_handled' in jdata) and ('is_ignored' in jdata):
            return jdata
        else:
            raise errors.MissingParamException('missing key params', None)


    @tornado.gen.coroutine
    def get(self, id=None):
        """
        @api {get} /file_event/:id       Get single file event
        @apiName GetFileEvent
        @apiGroup File Event

        @apiSuccess {Number}    id                  File event id
        @apiSuccess {String}    event               Event behave: created/moved/modified/deleted
        @apiSuccess {String}    path                File path
        @apiSuccess {String}    type                file/directory
        @apiSuccess {String}    event_time          When this file event happened
        @apiSuccess {Boolean}   is_handled          Flag if this event has been handled
        @apiSuccess {Boolean}   is_ignored          Flag if should ignore this event when display
        @apiSuccess {String}    reason              Reason for this record
        @apiSuccess {String}    created             When this record is created
        @apiSuccess {String}    modified            When this record is recently modified

        @apiSuccessExample {json} Success-Response:
            HTTP/1.1 200 OK
            {
                "id": 4,
                "event": "created",
                "path": "/Users/ywang/workspace/python/pycharm/zyWAF_AT_test/doc/api_project.json",
                "type": "file",
                "event_time": "2018-11-05 10:34:16",
                "is_handled": false,
                "is_ignored": false,
                "reason": null,
                "created": "2018-11-05 10:34:16",
                "modified": null
            }
        """
        try:
            retval = self.db.read_file_event_by_id(id)
            self.write(retval)
        except Exception as e:
            err = self.handle_db_error_msg(e)
            retval = self.format_api_return(error=err)
            self.write(retval)


    @tornado.gen.coroutine
    def put(self, id=None):
        """
        @api {get} /file_event/:id       Change single file event
        @apiName PutFileEvent
        @apiGroup File Event

        @apiParam {string}      is_handled          Flag if this event has been handled
        @apiParam {string}      is_ignored          Flag if should ignore this event when display

        @apiSuccess {Number}    id                  File event id
        @apiSuccess {String}    event               Event behave: created/moved/modified/deleted
        @apiSuccess {String}    path                File path
        @apiSuccess {String}    type                file/directory
        @apiSuccess {String}    event_time          When this file event happened
        @apiSuccess {Boolean}   is_handled          Flag if this event has been handled
        @apiSuccess {Boolean}   is_ignored          Flag if should ignore this event when display
        @apiSuccess {String}    reason              Reason for this record
        @apiSuccess {String}    created             When this record is created
        @apiSuccess {String}    modified            When this record is recently modified

        @apiSuccessExample {json} Success-Response:
            HTTP/1.1 200 OK
            {
                "id": 4,
                "event": "created",
                "path": "/Users/ywang/workspace/python/pycharm/zyWAF_AT_test/doc/api_project.json",
                "type": "file",
                "event_time": "2018-11-05 10:34:16",
                "is_handled": false,
                "is_ignored": false,
                "reason": null,
                "created": "2018-11-05 10:34:16",
                "modified": null
            }
        """
        try:
            jdata = self.get_params()
            jdata['id'] = id
            retval = self.db.update_file_event(jdata)
            self.write(retval)
        except Exception as e:
            err = self.handle_db_error_msg(e)
            retval = self.format_api_return(error=err)
            self.write(retval)


    @tornado.gen.coroutine
    def delete(self, id=None):
        self.db.test()

