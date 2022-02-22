from data.access.get.get import Get
from helpers.exceptions import get_exceptions as excepts
from helpers.logging.console_broadcast import ConsoleBroadcast


class RedisGet(Get):
    def get_data(self, get_query):
        for query in get_query:
            redis_output = self.apply_query(query)
            if redis_output is not None:
                self._cache.append(redis_output.decode())
        return self._cache

    def apply_query(self, query):
        key = list(query.keys())[0]
        values = list(query.values())[0]
        if str(key).lower() == 'get':
            try:
                output = self._connection_obj.get(str(values))
                ConsoleBroadcast.print_internal_message(f'value of {values} is accessed successfully!')
                if output is None:
                    raise excepts.EmptyQueryResult
            except excepts.EmptyQueryResult as e:
                e.evoke(query)
            except Exception as e:
                excepts.VitalGetException.evoke(e)

            if output is not None:
                return output
            else:
                return None

        if str(key).lower() == 'set':
            self._connection_obj.set(str(values[0]), str(values[1]))
            ConsoleBroadcast.print_internal_message(f'value of {values[0]} is set successfully!')
            return None
