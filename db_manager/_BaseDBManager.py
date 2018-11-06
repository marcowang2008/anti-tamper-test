from errors import NotImplementException

class BaseDBManager(object):

    def read_file_event_by_id(self, id):
        """
        :param id: integer
        :return: FileEvent in json
        """
        raise NotImplementException("not implement", None)


    def update_file_event(self, file_event):
        """
        :param file_event: dict of a file_event, allow to update is_handled and is_ignored column only
        :return: FileEvent in json
        """
        raise NotImplementException("not implement", None)


    def read_file_events_by_page(self, page, row_per_page):
        """
        :param page: page number
        :param row_per_page: row per page
        :return: list of FileEvent in json
        """
        raise NotImplementException("not implement", None)


    def create_file_event(self, behave, path, event_time, type):
        """
        :param behave: deleted/modified/moved
        :param path: file path
        :param event_time: when event happens
        :param type: file/folder
        :return: FileEvent in json
        """
        raise NotImplementException("not implement", None)










