from helpers.console.printing import ConsoleHelper
from data.connect.connections import Connection
from helpers.exceptions import connections_exceptions as excepts
import os
import pickle


class PickleConnection(Connection):
    def __init__(self, **kwargs):
        super(PickleConnection, self).__init__(**kwargs)
        self._pickle_address = kwargs['pickle_address'] if 'pickle_address' in kwargs else None
        self.check_on_construction_inputs()

    def check_on_construction_inputs(self):
        try:
            super(PickleConnection, self).check_on_construction_inputs()
            if self._pickle_address is None:
                raise excepts.NoNumpyAddress
            if not self.check_pickle_address():
                raise excepts.WrongCSVAddress
            if not self.check_pickle_type():
                raise excepts.NoCSVType
        except excepts.ConnectionException as e:
            e.evoke()
        except:
            excepts.VitalConnectionException().evoke()
        finally:
            pass

    def check_pickle_address(self):
        return os.path.isfile(self._pickle_address)

    def check_pickle_type(self):
        return os.path.splitext(self._pickle_address)[1] == '.pkl'

    def build_connection(self):
        try:
            self._connection_obj = self._pickle_address
            pickle.load(self._pickle_address)

            with open(self._pickle_address, "rb") as input_file:
                pickle.load(input_file)

        except Exception as e:
            excepts.VitalConnectionException().evoke(e)
        finally:
            pass
        super(PickleConnection, self).build_connection()

    def get_pickle_address(self):
        return self._pickle_address
