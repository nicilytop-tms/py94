def only_opened_file(func):
    def wrap(*args, **kwargs):
        self = args[0]
        if self.status_file == self.STATUSES_FILE[1]:
            raise ValueError('This file already closed')

        return func(*args, **kwargs)

    return wrap
