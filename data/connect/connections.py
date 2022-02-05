from helpers.exceptions import connections_exceptions as excepts
from helpers.console.printing import ConsoleHelper


class Connection:
    def __init__(self, **kwargs):
        self._connection_id = kwargs['connection_id'] if 'connection_id' in kwargs else None
        ConsoleHelper.define_connection('start', self._connection_id)
        self._connection_obj = None

    def check_on_construction_inputs(self):
        try:
            if self._connection_id is None:
                raise excepts.NoIDError
        except excepts.ConnectionException as e:
            e.evoke()
        except:
            excepts.VitalConnectionException().evoke()
        finally:
            pass

    def build_connection(self):
        ConsoleHelper.confirm_connection(self._connection_id)
        ConsoleHelper.define_connection('end', self._connection_id)
        # generate connection object according to the specific connection
        self._connection_obj = []

    def get_id(self):
        return self._connection_id
