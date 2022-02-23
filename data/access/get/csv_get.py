from data.access.get.get import Get
import pandas as pd
from helpers.exceptions import get_exceptions as excepts


class CSVGet(Get):

    def get_data(self):
        try:
            self._cache = pd.read_csv(self._connection_obj)
        except Exception as e:
            excepts.VitalGetException(self._loggers).evoke(e)

        return self._cache
