from data.connect.sql_database_connection import SQLDatabaseConnection
from helpers.exceptions import connections_exceptions as excepts
from helpers.console.printing import ConsoleHelper
import mysql.connector


class MYSQLConnection(SQLDatabaseConnection):
    def __init__(self, **kwargs):
        super(MYSQLConnection, self).__init__(**kwargs)
        self._port = kwargs['port'] if 'port' in kwargs else None
        self.check_on_construction_inputs()

    def check_on_construction_inputs(self):
        super(MYSQLConnection, self).check_on_construction_inputs()
        try:
            pass
            if self._port is None:
                raise excepts.NoRelationalDBPort
        except excepts.ConnectionException as e:
            e.evoke()
        except:
            excepts.VitalConnectionException().evoke()

    def build_connection(self):
        try:
            self._connection_obj = mysql.connector.connect(
                host=self._server,
                user=self._username,
                password=self._password,
                database=self._database,
                port=self._port
            )

        except mysql.connector.Error as e:
            excepts.RelationalDBConnectionError().evoke(f"Pyodbc error code: {0} | error description: {e}!")
        except:
            excepts.VitalConnectionException().evoke()
        finally:
            pass

        super(MYSQLConnection, self).build_connection()
