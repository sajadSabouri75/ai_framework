from data.connect.sql_database_connection import SQLDatabaseConnection
from helpers.exceptions import connections_exceptions as excepts
from helpers.console.printing import ConsoleHelper
import pyodbc


class MYSQLConnection(SQLDatabaseConnection):
    def __init__(self, **kwargs):
        super(MYSQLConnection, self).__init__(**kwargs)
        self._driver = kwargs['driver'] if 'driver' in kwargs else None
        self._port = kwargs['port'] if 'port' in kwargs else None
        self.check_on_construction_inputs()

    def check_on_construction_inputs(self):
        super(MYSQLConnection, self).check_on_construction_inputs()
        try:
            if self._driver is None:
                raise excepts.NoMSSQLServerDriver
            if self._port is None:
                raise excepts.NoRelationalDBPort
        except excepts.ConnectionException as e:
            e.evoke()
        except:
            excepts.VitalConnectionException().evoke()

    def build_connection(self):
        ConsoleHelper.print_internal_message('connection entries are confirmed! Trying to build the connection ...')
        try:
            port_string = f';port={self._port}' if self._port is not None else ''
            self._connection_obj = pyodbc.connect(
                f'DRIVER={self._driver};' +
                f'SERVER={self._server};' +
                f'DATABASE={self._database};' +
                f'UID={self._username};' +
                f'PWD={self._password}' +
                port_string
                # autocommit=True -> I don't know what this does. Needs to be checked.
            ).cursor()
        except pyodbc.Error as e:
            excepts.RelationalDBConnectionError().evoke(f"Pyodbc error code: {e.args[0]} | error description: {e.args[1]}!")
        except:
            excepts.VitalConnectionException().evoke()
        finally:
            pass

        super(MYSQLConnection).build_connection()
