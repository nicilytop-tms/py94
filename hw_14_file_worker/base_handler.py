class BaseHandler:
    def __init__(self, path):
        self.__path = path
        self.file = open(self.__path)

    @property
    def path(self):
        return self.__path

    def read(self):
        raise NotImplementedError

    def close(self):
        raise NotImplementedError

    def append(self, content):
        raise NotImplementedError
