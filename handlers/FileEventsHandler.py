import tornado.web
from handlers._BaseHandler import BaseHandler


class FileEventsHandler(BaseHandler):

    @tornado.gen.coroutine
    def get(self):
        """
        @api {get} /file_events?page=0&row_per_page=2       Get a list of file event
        @apiName file_events
        @apiGroup File Event

        @apiSuccess {Object[]}  data                    List of FileEvent
        @apiSuccess {Number}    data.id                 File event id
        @apiSuccess {String}    data.event              Event behave: created/moved/modified/deleted
        @apiSuccess {String}    data.path               File path
        @apiSuccess {String}    data.type               file/directory
        @apiSuccess {String}    data.event_time         When this file event happened
        @apiSuccess {Boolean}   data.is_handled         Flag if this event has been handled
        @apiSuccess {Boolean}   data.is_ignored         Flag if should ignore this event when display
        @apiSuccess {String}    data.reason             Reason for this record
        @apiSuccess {String}    data.created            When this record is created
        @apiSuccess {String}    data.modified           When this record is recently modified
        @apiSuccess {Number}    page                    Page number
        @apiSuccess {Number}    row_per_page            Row per page

        @apiSuccessExample {json} Success-Response:
            HTTP/1.1 200 OK
            {
                "data": [
                    {
                        "id": 3,
                        "event": "deleted",
                        "path": "/Users/ywang/workspace/python/pycharm/zyWAF_AT_test/doc/api_project.json",
                        "type": "file",
                        "event_time": "2018-11-05 10:34:16",
                        "is_handled": false,
                        "is_ignored": false,
                        "reason": null,
                        "created": "2018-11-05 10:34:16",
                        "modified": null
                    },
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
                ],
                "page": 1,
                "row_per_page": 2
            }
        """
        try:
            page = int(self.get_argument('page', 0))
            row_per_page = int(self.get_argument('row_per_page', 20))
            retval = {
                'data': self.db.read_file_events_by_page(page, row_per_page),
                'page': page,
                'row_per_page': row_per_page
            }
            self.write(retval)
        except Exception as e:
            err = self.handle_db_error_msg(e)
            retval = self.format_api_return(error=err)
            self.write(retval)


