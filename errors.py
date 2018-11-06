NO_ERROR                = { 'ecode': '0', 'emsg': None }
UNDEFINED_ERROR         = { 'ecode': '000', 'emsg': 'undefined error' }

# 1XX code is related to request
REQ_MISSING_PARAM       = { 'ecode': '100', 'emsg': 'key parameter missing' }
REQ_INVALID_PARAM       = { 'ecode': '101', 'emsg': 'invalid parameter value' }

# 2XX code for db related error
DB_ERROR                = { 'ecode': '200', 'emsg': 'database error' }
DB_MORE_THAN_ONE_RESULT = { 'ecode': '201', 'emsg': 'more than one result are found. expect only one.' }
DB_NO_RESULT            = { 'ecode': '202', 'emsg': 'no result is found. expect only one.' }
DB_TRANSACTION_FAILED   = { 'ecode': '203', 'emsg': 'transaction failed.' }
DB_ITEM_EXIST           = { 'ecode': '204', 'emsg': 'item already exist.' }
DB_DUPLICATE_ITEM       = { 'ecode': '205', 'emsg': 'duplicate item found.'}



class NotImplementException(Exception):
    def __init__(self, message, errors):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)
        # Now for your custom code...
        self.errors = errors


class MissingParamException(Exception):
    def __init__(self, message, errors):
        super().__init__(message)
        self.errors = errors