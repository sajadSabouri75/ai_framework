from data.connect.connections import Connection
from helpers.exceptions import connections_exceptions as excepts


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
                raise excepts.NoRelationalDBUsername(self._loggers)
            if self._password is None:
                raise excepts.NoRelationalDBPassword(self._loggers)
            if self._server is None:
                raise excepts.NoRelationalDBServer(self._loggers)
            if self._database is None:
                raise excepts.NoRelationalDBDatabase(self._loggers)
        except excepts.ConnectionException as e:
            e.evoke()
        except Exception as e:
            excepts.VitalConnectionException(self._loggers).evoke(e)
        finally:
            pass
