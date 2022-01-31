from helpers.exceptions import connections_exceptions as excepts
from helpers.console.printing import ConsoleHelper
import os


class Connection:
    def __init__(self, **kwargs):
        ConsoleHelper.define_connection('start')
        self._connection_id = kwargs['connection_id'] if 'connection_id' in kwargs else None

        self._connection_obj = None

    def check_on_construction_inputs(self):
        try:
            if self._connection_id is None:
                raise excepts.NoIDError
        except excepts.NoTypeError:
            excepts.NoTypeError.evoke()
        except excepts.NoIDError:
            excepts.NoIDError.evoke()
        except excepts.ConnectionException:
            excepts.ConnectionException.evoke()
        finally:
            pass

    def build_connection(self):
        ConsoleHelper.define_connection('end')

    def get_id(self):
        return self._connection_id


class CSVConnection(Connection):
    def __init__(self, **kwargs):
        super(CSVConnection, self).__init__(**kwargs)
        self._csv_address = kwargs['csv_address'] if 'csv_address' in kwargs else None
        self.check_on_construction_inputs()

    def check_on_construction_inputs(self):
        try:
            super(CSVConnection, self).check_on_construction_inputs()
            if self._csv_address is None:
                raise excepts.NoCSVAddress
            if not self.check_csv_address():
                raise excepts.WrongCSVAddress
            if not self.check_csv_type():
                raise excepts.NoCSVType

        except excepts.NoCSVAddress:
            excepts.NoCSVAddress.evoke()
        except excepts.WrongCSVAddress:
            excepts.WrongCSVAddress.evoke()
        except excepts.NoCSVType:
            excepts.NoCSVType.evoke()

        finally:
            pass

    def check_csv_address(self):
        return os.path.isfile(self._csv_address)

    def check_csv_type(self):
        return os.path.splitext(self._csv_address) == 'csv'

    def build_connection(self):
        print('')

        super(CSVConnection, self).build_connection()