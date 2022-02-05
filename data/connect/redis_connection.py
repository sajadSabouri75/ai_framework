from data.connect.nosql_database_connection import NoSQLDatabaseConnection
from helpers.exceptions import connections_exceptions as excepts
from helpers.console.printing import ConsoleHelper
import redis


class RedisConnection(NoSQLDatabaseConnection):
    def __init__(self, **kwargs):
        super(RedisConnection, self).__init__(**kwargs)
        self.check_on_construction_inputs()

    def check_on_construction_inputs(self):
        super(RedisConnection, self).check_on_construction_inputs()
        try:
            pass
        except excepts.ConnectionException as e:
            e.evoke()
        except:
            excepts.VitalConnectionException().evoke()

    def build_connection(self):
        ConsoleHelper.print_internal_message('connection entries are confirmed! Trying to build the connection ...')
        try:
            self._connection_obj = redis.Redis(
                f'host={self._host};' +
                f'port={self._port};' +
                f'password={self._password};'
            )
        except:
            excepts.VitalConnectionException().evoke()
        finally:
            pass

        super(RedisConnection, self).build_connection()
