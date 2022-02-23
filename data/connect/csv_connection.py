from data.connect.connections import Connection
from helpers.exceptions import connections_exceptions as excepts
import os
import pandas as pd
import pandas.errors


class CSVConnection(Connection):
    def __init__(self, **kwargs):
        super(CSVConnection, self).__init__(**kwargs)
        self._csv_address = kwargs['csv_address'] if 'csv_address' in kwargs else None
        self.check_on_construction_inputs()

    def check_on_construction_inputs(self):
        try:
            super(CSVConnection, self).check_on_construction_inputs()
            if self._csv_address is None:
                raise excepts.NoCSVAddress(self._loggers)
            if not self.check_csv_address():
                raise excepts.WrongCSVAddress(self._loggers)
            if not self.check_csv_type():
                raise excepts.NoCSVType(self._loggers)
        except excepts.ConnectionException as e:
            e.evoke()
        except Exception as e:
            excepts.VitalConnectionException(self._loggers).evoke()
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
            excepts.CSVEmpty(self._loggers).evoke()
        except Exception as e:
            excepts.VitalConnectionException(self._loggers).evoke(e)
        finally:
            pass
        super(CSVConnection, self).build_connection()

    def get_csv_address(self):
        return self._csv_address
