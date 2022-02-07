from helpers.exceptions.base_exceptions import AIFrameworkExceptions
from helpers.console.printing import ConsoleHelper


class ConnectionException(AIFrameworkExceptions):
    @staticmethod
    def evoke():
        ConsoleHelper.print_error("Something went wrong with this connection, don't know what!")
        exit() # default behavior is vital error (no fault tolerance)


class TrivialConnectionException(ConnectionException):
    @staticmethod
    def evoke():
        ConsoleHelper.print_warning('Some trivial process went wrong!')


class NoConnectionType(ConnectionException):
    @staticmethod
    def evoke():
        ConsoleHelper.print_error('Connection type must be defined. Use ConnectionTypes enumeration!')
        exit()


class NoValidConnectionType(ConnectionException):
    @staticmethod
    def evoke():
        ConsoleHelper.print_error('Connection type is not included in ConnectionTypes enumeration!')
        exit()


class NoConnectionName(ConnectionException):
    @staticmethod
    def evoke():
        ConsoleHelper.print_warning('Connection name is not defined. An automatic connection name would be generated!')


class DuplicateConnectionName(ConnectionException):
    @staticmethod
    def evoke():
        ConsoleHelper.print_warning('Connection name is duplicate! An automatic connection name would be generated!')


class VitalConnectionException(ConnectionException):
    @staticmethod
    def evoke():
        ConsoleHelper.print_error('Some vital process went wrong!')
        exit()


class NoTypeError(VitalConnectionException):
    @staticmethod
    def evoke():
        ConsoleHelper.print_error('No connection type defined!')
        exit()


class NoIDError(VitalConnectionException):
    @staticmethod
    def evoke():
        ConsoleHelper.print_error('No valid ID for this connection!')
        exit()


class NoCSVAddress(VitalConnectionException):
    @staticmethod
    def evoke():
        ConsoleHelper.print_error('No CSV file address provided!')
        exit()


class WrongCSVAddress(VitalConnectionException):
    @staticmethod
    def evoke():
        ConsoleHelper.print_error('CSV file address seems incorrect!')
        exit()


class NoCSVType(VitalConnectionException):
    @staticmethod
    def evoke():
        ConsoleHelper.print_error('The specified file is not CSV.')
        exit()


class CSVEmpty(VitalConnectionException):
    @staticmethod
    def evoke():
        ConsoleHelper.print_error('CSV file is empty!')
        exit()


class RelationalDBConnectionError(VitalConnectionException):
    @staticmethod
    def evoke(external_error):
        ConsoleHelper.print_error(external_error)
        exit()


class NoRelationalDBPort(TrivialConnectionException):
    @staticmethod
    def evoke():
        ConsoleHelper.print_warning('Port is not specified. Most of the times the default port is OK!')


class NoRelationalDBUsername(VitalConnectionException):
    @staticmethod
    def evoke():
        ConsoleHelper.print_error('The username for sql database connection is not defined!')
        exit()


class NoRelationalDBPassword(VitalConnectionException):
    @staticmethod
    def evoke():
        ConsoleHelper.print_error('The password for sql database connection is not defined!')
        exit()


class NoRelationalDBServer(VitalConnectionException):
    @staticmethod
    def evoke():
        ConsoleHelper.print_error('No specific server is defined for sql database connection!')
        exit()


class NoRelationalDBDatabase(VitalConnectionException):
    @staticmethod
    def evoke():
        ConsoleHelper.print_error('No specific database is defined for sql database connection!')
        exit()


class NoMSSQLServerDriver(VitalConnectionException):
    @staticmethod
    def evoke():
        ConsoleHelper.print_error('No driver is defined fo SQL server connection!')
        exit()


class NoSQLDBConnectionError(VitalConnectionException):
    @staticmethod
    def evoke(external_error):
        ConsoleHelper.print_error(external_error)
        exit()


class NoNoSQLHost(TrivialConnectionException):
    @staticmethod
    def evoke():
        ConsoleHelper.print_warning('No host is defined for database connection! Set to default host "localhost"')


class NoNoSQLPort(VitalConnectionException):
    @staticmethod
    def evoke():
        ConsoleHelper.print_error('No port is defined for database connection!')
        exit()


class NoNoSQLPassword(VitalConnectionException):
    @staticmethod
    def evoke():
        ConsoleHelper.print_error('No Password is defined for database connection!')
        exit()


class NoNoSQLDatabaseIndex(VitalConnectionException):
    @staticmethod
    def evoke():
        ConsoleHelper.print_error('No database index is defined!')
