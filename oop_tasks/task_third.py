class PostgresDBMS:
    working = True


class AbstractManagerConnector:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def connect(self):
        raise NotImplementedError


class PGManagerConnector(AbstractManagerConnector):
    @classmethod
    def create(cls, url):
        """
        Создать метод create таким образом, что бы мы получали надпись ->
        psql://username:password@127.0.0.1:5432/db в том случае если,
        аргумент working класса PostgresDBMS имеет значение True
        И получать надпись -> Connection refused если это значение равно False
        """

    def connect(self):
        print(f'Connected to psql://{self.username}:{self.password}@{self.host}:{self.port}/{self.db}')
        print('Connection refused')


pg_connector = PGManagerConnector.create('psql://username:password@127.0.0.1:5432/db')
pg_connector.connect()
