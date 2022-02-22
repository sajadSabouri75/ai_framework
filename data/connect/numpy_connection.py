from data.connect.connections import Connection
from helpers.exceptions import connections_exceptions as excepts
import os
import numpy as np


class NumpyConnection(Connection):
    def __init__(self, **kwargs):
        super(NumpyConnection, self).__init__(**kwargs)
        self._numpy_address = kwargs['numpy_address'] if 'numpy_address' in kwargs else None
        self.check_on_construction_inputs()

    def check_on_construction_inputs(self):
        try:
            super(NumpyConnection, self).check_on_construction_inputs()
            if self._numpy_address is None:
                raise excepts.NoNumpyAddress
            if not self.check_numpy_address():
                raise excepts.WrongNumpyAddress
            if not self.check_numpy_type():
                raise excepts.NoNumpyType
        except excepts.ConnectionException as e:
            e.evoke()
        except:
            excepts.VitalConnectionException().evoke()
        finally:
            pass

    def check_numpy_address(self):
        return os.path.isfile(self._numpy_address)

    def check_numpy_type(self):
        return os.path.splitext(self._numpy_address)[1] == '.npy'

    def build_connection(self):
        try:
            self._connection_obj = self._numpy_address
            np.load(self._numpy_address)
        except np.errors.EmptyDataError:
            excepts.NumpyEmpty().evoke()
        except Exception as e:
            excepts.VitalConnectionException().evoke(e)
        finally:
            pass
        super(NumpyConnection, self).build_connection()

    def get_numpy_address(self):
        return self._numpy_address
