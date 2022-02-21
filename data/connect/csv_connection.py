import pandas.errors
from helpers.console.printing import ConsoleHelper
from data.connect.connections import Connection
from helpers.exceptions import connections_exceptions as excepts
import os
import pandas as pd


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
        except excepts.ConnectionException as e:
            e.evoke()
        except:
            excepts.VitalConnectionException().evoke()
        finally:
            pass

    def check_csv_address(self):
        return os.path.isfile(self._csv_address)

    def check_csv_type(self):
        return os.path.splitext(self._csv_address)[1] == '.csv'

    def build_connection(self):
        try:
            self._connection_obj = self._csv_address
            pd.read_csv(self._csv_address)
        except pd.errors.EmptyDataError:
            excepts.CSVEmpty().evoke()
        except:
            excepts.VitalConnectionException().evoke()
        finally:
            pass
        super(CSVConnection, self).build_connection()

    def get_csv_address(self):
        return self._csv_address
