from data.connect.nosql_database_connection import NoSQLDatabaseConnection
from helpers.exceptions import base_exceptions as base_excepts
from helpers.exceptions import connections_exceptions as excepts
from helpers.console.printing import ConsoleHelper
import redis


class RedisConnection(NoSQLDatabaseConnection):
    def __init__(self, **kwargs):
        super(RedisConnection, self).__init__(**kwargs)
        self._db_index = kwargs['db_index'] if 'db_index' in kwargs else None
        self.check_on_construction_inputs()

    def check_on_construction_inputs(self):
        super(RedisConnection, self).check_on_construction_inputs()
        try:
            if self._db_index is None:
                raise excepts.NoNoSQLDatabaseIndex
        except excepts.ConnectionException as e:
            e.evoke()
        except:
            excepts.VitalConnectionException().evoke()

    def build_connection(self):
        try:
            self._connection_obj = redis.Redis(
                host=self._host,
                port=self._port,
                db=self._db_index,
                password=self._password
            )
            e = self.check_initial_connection()
            raise e
        except redis.exceptions.ConnectionError as e:
            excepts.NoSQLDBConnectionError().evoke(f'Redis error description: {e}')
        except excepts.ConnectionException as e:
            e.evoke()
        except base_excepts.NoException as e:
            e.evoke()
        except Exception as e:
            excepts.VitalConnectionException().evoke(e)
        finally:
            pass

        super(RedisConnection, self).build_connection()

    def check_initial_connection(self):
        try:
            self._connection_obj.set('$name$', 'unknown')
            self._connection_obj.get('$name$')
            return base_excepts.NoException
        except Exception as e:
            return e
