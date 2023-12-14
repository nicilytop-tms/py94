import json

from hw_14_file_worker.base_handler import BaseHandler
from hw_14_file_worker.decorators import only_opened_file


class JsonHandler(BaseHandler):
    STATUSES_FILE = ('OPENED', 'CLOSED')

    def __init__(self, path):
        super().__init__(path)
        self.content = json.load(self.file)

        if not isinstance(self.content, list):
            raise TypeError('This json format unsupportable')

        self.status_file = self.STATUSES_FILE[0]

    @only_opened_file
    def read(self):
        return self.content

    @only_opened_file
    def append(self, content):
        self.content.append(content)

    def close(self):
        if self.file.mode == 'r':
            self.file.close()
            self.file = open(self.path, 'w')

        json.dump(self.content, self.file)
        self.file.close()
        self.status_file = self.STATUSES_FILE[1]
