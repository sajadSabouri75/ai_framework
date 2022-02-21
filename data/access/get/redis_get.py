from data.access.get.get import Get
from helpers.console.printing import ConsoleHelper


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
            output = self._connection_obj.get(str(values))
            ConsoleHelper.print_internal_message(f'value of {values} is accessed successfully!')
            return output
        if str(key).lower() == 'set':
            self._connection_obj.set(str(values[0]), str(values[1]))
            ConsoleHelper.print_internal_message(f'value of {values[0]} is set successfully!')
            return None
