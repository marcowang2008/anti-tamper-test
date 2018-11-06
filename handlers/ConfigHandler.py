import tornado.web
from handlers._BaseHandler import BaseHandler

class ConfigHandler(BaseHandler):

    @tornado.gen.coroutine
    def get(self):
        """
        @api {get} /configs Get call Configs
        @apiName GetConfigs
        @apiGroup Gonfig

        @apiSuccess {Object[]}      configs                             List of configs
        @apiSuccess {String}        configs.name                        Config name
        @apiSuccess {Boolean}       configs.useAlternate                Whether use alternative source for file diff check
        @apiSuccess {Object}        configs.monitored                   Monitored source server connection info
        @apiSuccess {String}        configs.monitored.password          Monitored source server connection password
        @apiSuccess {String}        configs.monitored.websiteFolder     Monitored file path on source server
        @apiSuccess {String}        configs.monitored.username          Monitored source server connection username
        @apiSuccess {String}        configs.monitored.host              Monitored source server ip
        @apiSuccess {String}        configs.monitored.port              Monitored source server port
        @apiSuccess {String}        configs.monitored.protocol          Monitored source server connection protocol
        @apiSuccess {Object[]}      configs.filters                     List of ignored file filters
        @apiSuccess {Boolean}       configs.filters.regex               Is this filter a regex
        @apiSuccess {String}        configs.filters.filter              Filter string
        @apiSuccess {Number}        configs.interval                    AT check interval
        @apiSuccess {Number}        configs.mode                        AT running mode
        @apiSuccess {String}        configs.lastUpdate                  Config last update time
        @apiSuccess {Number}        configs.heartbeat                   AT check source server connection interval
        @apiSuccess {Object}        configs.alternate                   Alternate source server connection info
        @apiSuccess {String}        configs.alternate.password          Alternate source server connection password
        @apiSuccess {String}        configs.alternate.websiteFolder     Alternate file path on source server
        @apiSuccess {String}        configs.alternate.username          Alternate source server connection username
        @apiSuccess {String}        configs.alternate.host              Alternate source server ip
        @apiSuccess {String}        configs.alternate.port              Alternate source server port
        @apiSuccess {String}        configs.alternate.protocol          Alternate source server connection protocol
        @apiSuccessExample {json} Success-Response:
            HTTP/1.1 200 OK
            [
                {
                    "name": "location1",
                    "useAlternate": false,
                    "monitored": {
                        "password": "password1",
                        "websiteFolder": "/",
                        "username": "user1",
                        "host": "1.1.1.1",
                        "port": 22,
                        "protocol": 0
                    },
                    "filters": [
                        {
                            "regex": false,
                            "filter": "*.txt"
                        }
                    ],
                    "interval": 600,
                    "mode": 0,
                    "lastUpdate": "",
                    "heartbeat": 30,
                    "alternate": {
                        "password": "password2",
                        "websiteFolder": "/",
                        "username": "user2",
                        "host": "1.1.1.2",
                        "port": 22,
                        "protocol": 0
                    }
                }
            ]
        """
        retval = {
            'version': 'v0.0.1'
        }
        self.write(retval)