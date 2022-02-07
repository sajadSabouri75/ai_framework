from helpers.generators.generators import Generator
from helpers.console.printing import ConsoleHelper
from helpers.exceptions import connections_exceptions as connection_excepts
from helpers.exceptions import get_exceptions as get_excepts
from data.connect.csv_connection import CSVConnection
from data.connect.sql_server_connection import SQLServerConnection
from data.connect.mysql_connection import MYSQLConnection
from data.connect.redis_connection import RedisConnection
from data.connect.connections_helpers import ConnectionsTypes


class AIShell:
    def __init__(self):
        self._generator = Generator()
        self._connections = []
        self._connections_ids = []
        self._connections_names = []
        self._connections_id_to_name_dict = {}
        self._connections_name_to_id_dict = {}

    # Connection generation
    def generate_connection(self, **kwargs):
        ConsoleHelper.define_connection('start')

        was_successful = True
        connection_type = kwargs['connection_type'] if 'connection_type' in kwargs else None
        connection_name = kwargs['connection_name'] if 'connection_name' in kwargs else None
        connection_name = self.check_on_generation_inputs(connection_type, connection_name)
        connection_id = self._generator.generate_connection_counter()

        if connection_type is ConnectionsTypes.CSV:
            self._connections.append(
                CSVConnection(
                    connection_id=connection_id,
                    connection_name=connection_name,
                    csv_address=kwargs['csv_address'] if 'csv_address' in kwargs else None
                )
            )
        elif connection_type is ConnectionsTypes.SQL_SERVER:
            self._connections.append(
                SQLServerConnection(
                    connection_id=connection_id,
                    connection_name=connection_name,
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
                    connection_id=connection_id,
                    connection_name=connection_name,
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
                    connection_id=connection_id,
                    connection_name=connection_name,
                    password=kwargs['password'] if 'password' in kwargs else None,
                    host=kwargs['host'] if 'host' in kwargs else None,
                    port=kwargs['port'] if 'port' in kwargs else None,
                    db_index=kwargs['database_index'] if 'database_index' in kwargs else None
                )
            )
        else:
            was_successful = False

        if was_successful:
            self._connections_id_to_name_dict[connection_id] = connection_name
            self._connections_name_to_id_dict[connection_name] = connection_id
            self._connections_ids.append(connection_id)
            self._connections_names.append(connection_name)
            ConsoleHelper.print_internal_message(f'connection [{connection_name}] entries are confirmed! Trying to build the connection ...')
            self._connections[-1].build_connection()

    def generate_auto_connection_name(self):
        return f'connection_{self._generator.get_connection_counter()+1}'

    def check_on_generation_inputs(self, connection_type, connection_name):
        try:
            if connection_type is None:
                raise connection_excepts.NoConnectionType
            elif not connection_type in ConnectionsTypes:
                raise connection_excepts.NoValidConnectionType
            elif connection_name is None:
                raise connection_excepts.NoConnectionName
            elif connection_name in self._connections_names:
                raise connection_excepts.DuplicateConnectionName
            else:
                return connection_name
        except connection_excepts.NoConnectionName as e:
            e.evoke()
            return self.generate_auto_connection_name()
        except connection_excepts.DuplicateConnectionName as e:
            e.evoke()
            return self.generate_auto_connection_name()
        except connection_excepts.ConnectionException as e:
            e.evoke()

    # Getting data
    def get_data(self, **kwargs):
        ConsoleHelper.define_get('start')
        connection_name = kwargs['connection_name'] if 'connection_name' in kwargs else None
        connection_id = kwargs['connection_id'] if 'connection_id' in kwargs else None
        connection, connection_name, connection_id = self.identify_connection(connection_name, connection_id)

    def get_connection_of_id(self, connection_id):
        return [connection for connection in self._connections if connection.get_id() == connection_id][0]

    def identify_connection(self, connection_name, connection_id):
        try:
            if connection_name is None and connection_id is None:
                raise get_excepts.NoIdentification
            if connection_name is not None:
                if not connection_name in self._connections_names:
                    raise get_excepts.InvalidName
            if connection_id is not None:
                if not connection_id in self._connections_ids:
                    raise get_excepts.InvalidID
            if connection_name is not None and connection_id is not None:
                valid_connection_name = self._connections_id_to_name_dict[connection_id]
                if valid_connection_name != connection_name:
                    raise get_excepts.InvalidNameIDPair

        except get_excepts.GetException as e:
            e.evoke()

        if connection_id is None:
            connection_id = self._connections_name_to_id_dict[connection_name]

        connection_name = self._connections_id_to_name_dict[connection_id]

        return self.get_connection_of_id(connection_id), connection_name, connection_id
