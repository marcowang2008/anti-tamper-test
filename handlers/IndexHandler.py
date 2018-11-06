import tornado.web
from handlers._BaseHandler import BaseHandler

class IndexHandler(BaseHandler):

    @tornado.gen.coroutine
    def get(self):
        """
        @api {get} /       Request API information
        @apiName Version
        @apiGroup Info

        @apiSuccess {String}    version     AT verison info
        @apiSuccessExample {json} Success-Response:
            HTTP/1.1 200 OK
            {
                "version": "v0.0.1"
            }
        """
        retval = {
            'version': 'v0.0.1'
        }
        self.write(retval)