from helpers.generators.generators import Generator
from data.connect.csv_connection import CSVConnection
from data.connect.sql_server_connection import SQLServerConnection
from data.connect.mysql_connection import MYSQLConnection
from data.connect.redis_connection import RedisConnection
from data.connect.connections_helpers import ConnectionsTypes


class AIShell:
    def __init__(self):
        self._generator = Generator()
        self._connections = []

    def generate_connection(self, connection_type, **kwargs):
        was_successful = True
        if connection_type is ConnectionsTypes.CSV:
            self._connections.append(
                CSVConnection(
                    connection_id=self._generator.generate_connection_counter(),
                    csv_address=kwargs['csv_address'] if 'csv_address' in kwargs else None
                )
            )
        elif connection_type is ConnectionsTypes.SQL_SERVER:
            self._connections.append(
                SQLServerConnection(
                    connection_id=self._generator.generate_connection_counter(),
                    username=kwargs['username'] if 'username' in kwargs else None,
                    password=kwargs['password'] if 'password' in kwargs else None,
                    server=kwargs['server'] if 'server' in kwargs else None,
                    database=kwargs['database'] if 'database' in kwargs else None,
                    driver=kwargs['driver'] if 'driver' in kwargs else None,
                )
            )
        elif connection_type is ConnectionsTypes.MY_SQL:
            self._connections.append(
                MYSQLConnection(
                    connection_id=self._generator.generate_connection_counter(),
                    username=kwargs['username'] if 'username' in kwargs else None,
                    password=kwargs['password'] if 'password' in kwargs else None,
                    server=kwargs['server'] if 'server' in kwargs else None,
                    database=kwargs['database'] if 'database' in kwargs else None,
                    driver=kwargs['driver'] if 'driver' in kwargs else None,
                    port=kwargs['port'] if 'port' in kwargs else None
                )
            )
        elif connection_type is ConnectionsTypes.REDIS:
            self._connections.append(
                RedisConnection(
                    connection_id=self._generator.generate_connection_counter(),
                    password=kwargs['password'] if 'password' in kwargs else None,
                    host=kwargs['host'] if 'host' in kwargs else None,
                    port=kwargs['port'] if 'port' in kwargs else None
                )
            )
        else:
            was_successful = False

        if was_successful:
            self._connections[-1].build_connection()
