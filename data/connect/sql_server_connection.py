from data.connect.connections import Connection
from helpers.exceptions import connections_exceptions as excepts
import pyodbc


class SQLDatabaseConnection(Connection):
    def __init__(self, **kwargs):
        super(SQLDatabaseConnection, self).__init__(**kwargs)
        self._username = kwargs['username'] if 'username' in kwargs else None
        self._password = kwargs['password'] if 'password' in kwargs else None
        self._server = kwargs['server'] if 'server' in kwargs else None
        self._database = kwargs['database'] if 'database' in kwargs else None

    def check_on_construction_inputs(self):
        super(SQLDatabaseConnection, self).check_on_construction_inputs()
        try:
            if self._username is None:
                raise excepts.NoRelationalDBUsername
            if self._password is None:
                raise excepts.NoRelationalDBPassword
            if self._server is None:
                raise excepts.NoRelationalDBServer
            if self._database is None:
                raise excepts.NoRelationalDBDatabase
        except excepts.ConnectionException as e:
            e.evoke()
        finally:
            pass


class SQLServerConnection(SQLDatabaseConnection):
    def __init__(self, **kwargs):
        super(SQLServerConnection, self).__init__(**kwargs)
        self._driver = kwargs['driver'] if 'driver' in kwargs else None
        self.check_on_construction_inputs()

    def check_on_construction_inputs(self):
        super(SQLServerConnection, self).check_on_construction_inputs()
        try:
            if self._driver is None:
                raise excepts.NoMSSQLServerDriver
        except excepts.ConnectionException as e:
            e.evoke()

    def build_connection(self):
        print('connection entries are confirmed! Trying to build the connection ...')
        try:
            self._connection_obj = pyodbc.connect(
                f'DRIVER={self._driver};' +
                f'SERVER={self._server};' +
                f'DATABASE={self._database};' +
                f'UID={self._username};' +
                f'PWD={self._password}',
                # autocommit=True -> I don't know what this does. Needs to be checked.
            )
        except pyodbc.Error as e:
            excepts.RelationalDBConnectionError().evoke(f"Pyodbc error code: {e.args[0]}!")

        super(SQLServerConnection, self).build_connection()
