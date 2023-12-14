from hw_14_file_worker.base_handler import BaseHandler


class TxtHandler(BaseHandler):
    def read(self):
        raise NotImplementedError

    def close(self):
        raise NotImplementedError

    def append(self, content):
        raise NotImplementedError
