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
