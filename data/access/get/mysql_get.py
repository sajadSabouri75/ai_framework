from data.access.get.get import Get
from helpers.logging.console_broadcast import ConsoleBroadcast
from helpers.exceptions import get_exceptions as excepts
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
        try:
            output = pd.read_sql(query, self._connection_obj)
            for logger in self._loggers:
                logger.print_internal_message(f'query "{query}" is performed successfully!')
            if output.empty:
                raise excepts.EmptyQueryResult(self._loggers)
        except excepts.EmptyQueryResult as e:
            e.evoke(query)
        except excepts.GetException as e:
            e.evoke()
        except Exception as e:
            excepts.VitalGetException(self._loggers).evoke(e)

        if not output.empty:
            return output
        else:
            return None
