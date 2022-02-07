
class Generator:
    def __init__(self):
        self._connection_counter = 0

    def generate_connection_counter(self):
        self._connection_counter += 1
        return self._connection_counter

    def get_connection_counter(self):
        return self._connection_counter