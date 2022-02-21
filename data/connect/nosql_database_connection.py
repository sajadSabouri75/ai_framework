from data.connect.connections import Connection
from helpers.exceptions import connections_exceptions as excepts


class NoSQLDatabaseConnection(Connection):
    def __init__(self, **kwargs):
        super(NoSQLDatabaseConnection, self).__init__(**kwargs)
        self._password = kwargs['password'] if 'password' in kwargs else None
        self._port = kwargs['port'] if 'port' in kwargs else None
        self._host = kwargs['host'] if 'host' in kwargs else None

    def check_on_construction_inputs(self):
        super(NoSQLDatabaseConnection, self).check_on_construction_inputs()
        try:
            if self._password is None:
                raise excepts.NoNoSQLPassword
            if self._port is None:
                raise excepts.NoNoSQLPort
            if self._host is None:
                raise excepts.NoNoSQLHost
        except excepts.ConnectionException as e:
            e.evoke()
        except Exception as e:
            excepts.VitalConnectionException().evoke(e)
        finally:
            pass
