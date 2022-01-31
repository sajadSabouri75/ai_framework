# Base database importer -> mainly focused on CRUD operation.


class BaseDBManager:
    def __init__(self, **kwargs):
        self._name = kwargs['name'] if 'name' in kwargs else 'unknown database'
        self._odbc_type = kwargs['source_type'] if 'source_type' in kwargs else None
        self._username = kwargs['username'] if 'username' in kwargs else None
        self._password = kwargs['password'] if 'password' in kwargs else None
        self._server = kwargs['server'] if 'server' in kwargs else None
        self._database = kwargs['database'] if 'database' in kwargs else None
        self._driver = kwargs['driver'] if 'driver' in kwargs else None
        self.check_necessary_inputs()

    def check_necessary_inputs(self):
        pass


    def print_db_stats(self):
        print('<database_manager_stats>')
        print(f'> db name: {self._name}')
