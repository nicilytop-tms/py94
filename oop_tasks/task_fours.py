class PostgresDBMS:
    working = True


class ReConnectorMixin:
    """
    Реализовать метод reconnect который вызван внизу у объекта менеджера, и
    - обеспечить его вызов путем использования парадигмы наследования без использования super
    таким образом что бы при его вызове на экран выводилось сообщение -> 'Reconnected' в случае если
    - атрибут working класса PostgresDBMS установлен в True
    и в случае если этот атрибут установлен в False выводить сообщение 'Already reconected'
    При этом обращаться напрямую к классу из метода reconnect - ЗАПРЕЩЕНО.

    PS - смотри атрибуты класса AbstractManagerConnector
    """


class AbstractManagerConnector:
    username = None
    password = None
    db = None
    dbms_system = PostgresDBMS

    def __init__(self, host, port):
        self.host = host
        self.port = port

    def connect(self):
        raise NotImplementedError


class PGManagerConnector(AbstractManagerConnector, ReConnectorMixin):
    @classmethod
    def create(cls, url):
        return cls('127.0.0.1', '5432')

    def connect(self):
        if PostgresDBMS.working:
            print(f'Connected to psql://{self.username}:{self.password}@{self.host}:{self.port}/{self.db}')
        else:
            print('Connection refused')


pg_connector = PGManagerConnector.create('psql://username:password@127.0.0.1:5432/db')
pg_connector.reconnect()

