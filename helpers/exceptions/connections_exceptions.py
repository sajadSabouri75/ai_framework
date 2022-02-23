from helpers.exceptions.base_exceptions import AIFrameworkExceptions
from helpers.logging.console_broadcast import ConsoleBroadcast


class ConnectionException(AIFrameworkExceptions):
    def evoke(self):
        for logger in self._loggers:
            logger.print_error("Something went wrong with this connection, don't know what!")
            logger.flush()
        exit()  # default behavior is vital error (zero fault tolerance)


class TrivialConnectionException(ConnectionException):
    def evoke(self):
        for logger in self._loggers:
            logger.print_warning('Some trivial process went wrong!')


class VitalConnectionException(ConnectionException):
    def evoke(self, message=''):
        for logger in self._loggers:
            logger.print_error('Some vital process went wrong!')
            if message != '':
                logger.print_error(message)
            logger.flush()

        exit()


class NoConnectionType(ConnectionException):
    def evoke(self):
        for logger in self._loggers:
            logger.print_error('Connection type must be defined. Use ConnectionTypes enumeration!')
            logger.flush()

        exit()


class NoValidConnectionType(ConnectionException):
    def evoke(self):
        for logger in self._loggers:
            logger.print_error('Connection type is not included in ConnectionTypes enumeration!')
            logger.flush()

        exit()


class NoConnectionName(ConnectionException):
    def evoke(self):
        for logger in self._loggers:
            logger.print_warning('Connection name is not defined. An automatic connection name would be generated!')


class DuplicateConnectionName(ConnectionException):
    def evoke(self):
        for logger in self._loggers:
            logger.print_warning('Connection name is duplicate! An automatic connection name would be generated!')


class NoTypeError(ConnectionException):
    def evoke(self):
        for logger in self._loggers:
            logger.print_error('No connection type defined!')
            logger.flush()
        exit()


class NoIDError(ConnectionException):
    def evoke(self):
        for logger in self._loggers:
            logger.print_error('No valid ID for this connection!')
            logger.flush()

        exit()


# CSV connection
class NoCSVAddress(ConnectionException):
    def evoke(self):
        for logger in self._loggers:
            logger.print_error('No CSV file address provided!')
            logger.flush()
        exit()


class WrongCSVAddress(ConnectionException):
    def evoke(self):
        for logger in self._loggers:
            logger.print_error('CSV file address seems incorrect!')
            logger.flush()
        exit()


class NoCSVType(ConnectionException):
    def evoke(self):
        for logger in self._loggers:
            logger.print_error('The specified file is not CSV.')
            logger.flush()
        exit()


class CSVEmpty(ConnectionException):
    def evoke(self):
        for logger in self._loggers:
            logger.print_warning('CSV file is empty!')


# Numpy connection
class NoNumpyAddress(ConnectionException):
    def evoke(self):
        for logger in self._loggers:
            logger.print_error('No numpy file address provided!')
            logger.flush()
        exit()


class WrongNumpyAddress(ConnectionException):
    def evoke(self):
        for logger in self._loggers:
            logger.print_error('Numpy file address seems incorrect!')
            logger.flush()
        exit()


class NoNumpyType(ConnectionException):
    def evoke(self):
        for logger in self._loggers:
            logger.print_error('The specified file is not numpy.')
            logger.flush()
        exit()


class NumpyEmpty(ConnectionException):
    def evoke(self):
        for logger in self._loggers:
            logger.print_warning('Numpy file is empty!')


# Pickle connection
class NoPickleAddress(ConnectionException):
    def evoke(self):
        for logger in self._loggers:
            logger.print_error('No pickle file address provided!')
            logger.flush()
        exit()


class WrongPickleAddress(ConnectionException):
    def evoke(self):
        for logger in self._loggers:
            logger.print_error('Pickle file address seems incorrect!')
            logger.flush()
        exit()


class NoPickleType(ConnectionException):
    def evoke(self):
        for logger in self._loggers:
            logger.print_error('The specified file is not pickle.')
            logger.flush()
        exit()


class PickleEmpty(ConnectionException):
    def evoke(self):
        for logger in self._loggers:
            logger.print_warning('Pickle file is empty!')


class RelationalDBConnectionError(ConnectionException):
    def evoke(self, external_error):
        for logger in self._loggers:
            logger.print_error(external_error)
            logger.flush()
        exit()


class NoRelationalDBPort(ConnectionException):
    def evoke(self):
        for logger in self._loggers:
            logger.print_warning('Port is not specified. Most of the times the default port is OK!')


class NoRelationalDBUsername(ConnectionException):
    def evoke(self):
        for logger in self._loggers:
            logger.print_error('The username for sql database connection is not defined!')
            logger.flush()
        exit()


class NoRelationalDBPassword(ConnectionException):
    def evoke(self):
        for logger in self._loggers:
            logger.print_error('The password for sql database connection is not defined!')
            logger.flush()
        exit()


class NoRelationalDBServer(ConnectionException):
    def evoke(self):
        for logger in self._loggers:
            logger.print_error('No specific server is defined for sql database connection!')
            logger.flush()
        exit()


class NoRelationalDBDatabase(ConnectionException):
    def evoke(self):
        for logger in self._loggers:
            logger.print_error('No specific database is defined for sql database connection!')
            logger.flush()
        exit()


class NoMSSQLServerDriver(ConnectionException):
    def evoke(self):
        for logger in self._loggers:
            logger.print_error('No driver is defined fo SQL server connection!')
            logger.flush()
        exit()


class NoSQLDBConnectionError(ConnectionException):
    def evoke(self, external_error):
        for logger in self._loggers:
            logger.print_error(external_error)
            logger.flush()
        exit()


class NoNoSQLHost(ConnectionException):
    def evoke(self):
        for logger in self._loggers:
            logger.print_warning('No host is defined for database connection! Set to default host "localhost"')


class NoNoSQLPort(ConnectionException):
    def evoke(self):
        for logger in self._loggers:
            logger.print_error('No port is defined for database connection!')
            logger.flush()
        exit()


class NoNoSQLPassword(ConnectionException):
    def evoke(self):
        for logger in self._loggers:
            logger.print_error('No Password is defined for database connection!')
            logger.flush()
        exit()


class NoNoSQLDatabaseIndex(ConnectionException):
    def evoke(self):
        for logger in self._loggers:
            logger.print_error('No database index is defined!')
