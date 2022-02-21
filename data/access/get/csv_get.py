from data.access.get.get import Get
import pandas as pd


class CSVGet(Get):

    def get_data(self):
        self._cache = pd.read_csv(self._connection_obj)
        return self._cache
