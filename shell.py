from helpers.generators.generators import Generator
from data.connect.connections import CSVConnection
from data.connect.connections_helpers import  ConnectionsTypes


class Shell:
    def __init__(self):
        self._generator = Generator()
        self._connections = []

    def generate_connection(self, connection_type, **kwargs):
        if connection_type is ConnectionsTypes.CSV:
            self._connections.append(
                CSVConnection(
                    connection_id=self._generator.generate_connection_counter(),
                    csv_address=kwargs['csv_address'] if 'csv_address' in kwargs else None
                )
            )

        self._connections[-1].build_connection()
