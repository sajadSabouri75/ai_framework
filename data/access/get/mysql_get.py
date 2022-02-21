from data.access.get.get import Get
from helpers.console.printing import ConsoleHelper
import pandas as pd


class MYSQLGet(Get):
    def get_data(self, get_query):
        self._connection_obj.cursor()
        for query in get_query:
            sql_server_output = self.apply_query(query)
            if sql_server_output is not None:
                self._cache.append(sql_server_output)
        return self._cache

    def apply_query(self, query):
        output = pd.read_sql(query, self._connection_obj)
        ConsoleHelper.print_internal_message(f'query "{query}" is performed successfully!')

        if not output.empty:
            return output
        else:
            return None
