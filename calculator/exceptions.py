class UnknownOperation(Exception):
    def __init__(self, operation=None):
        self.operation = operation

    def __str__(self):
        if self.operation:
            return f'Unknown operation like this: {self.operation}'
        return 'Unknown operation'


class NotNumberError(Exception):
    ...
