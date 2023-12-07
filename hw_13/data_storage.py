class DataStorage:
    def __init__(self, path_to_file):
        self.__path = path_to_file
        self.status = 'disconected'
        self.content = None
        self.file = None

    @property
    def path(self):
        return self.__path

    def _create_storage(self):
        self.file = open(self.path, 'w')
        return self.file

    def connect(self):
        try:
            self.file = open(self.path, 'r')
            self.content = self.file.read()
            self.status = 'connected'
            return self.file
        except FileNotFoundError:
            self._create_storage()
            self.status = 'connected'
            return self.file

    def disconnect(self):
        self.file.close()
        print('File was closed')


class DataStorageWrite(DataStorage):
    def _create_storage(self):
        super()._create_storage()

    def connect(self):
        super().connect()
        self.disconnect()
        self.file = open(self.path, 'a')

    def append(self, additional_content):
        self.file.write(additional_content)
