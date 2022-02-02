from helpers.exceptions.base_exceptions import AIFrameworkExceptions
from helpers.console.printing import ConsoleHelper


class ConnectionException(AIFrameworkExceptions):
    @staticmethod
    def evoke():
        ConsoleHelper.print_error("Something went wrong with this connection, don't know what!")
        exit()


class VitalConnectionException(ConnectionException):
    @staticmethod
    def evoke():
        ConsoleHelper.print_error('Some vital process went wrong!')


class NoTypeError(ConnectionException):
    @staticmethod
    def evoke():
        ConsoleHelper.print_error('No connection type defined!')
        exit()


class NoIDError(ConnectionException):
    @staticmethod
    def evoke():
        ConsoleHelper.print_error('No valid ID for this connection!')
        exit()


class NoCSVAddress(ConnectionException):
    @staticmethod
    def evoke():
        ConsoleHelper.print_error('No CSV file address provided!')
        exit()


class WrongCSVAddress(ConnectionException):
    @staticmethod
    def evoke():
        ConsoleHelper.print_error('CSV file address seems incorrect!')
        exit()


class NoCSVType(ConnectionException):
    @staticmethod
    def evoke():
        ConsoleHelper.print_error('The specified file is not CSV.')
        exit()


class CSVEmpty(ConnectionException):
    @staticmethod
    def evoke():
        ConsoleHelper.print_error('CSV file is empty!')
        exit()

class RelationalDBConnectionError(ConnectionException):
    @staticmethod
    def evoke(external_error):
        ConsoleHelper.print_error(external_error)
        exit()


class NoRelationalDBUsername(ConnectionException):
    @staticmethod
    def evoke():
        ConsoleHelper.print_error('The username for sql database connection is not defined!')
        exit()


class NoRelationalDBPassword(ConnectionException):
    @staticmethod
    def evoke():
        ConsoleHelper.print_error('The password for sql database connection is not defined!')
        exit()


class NoRelationalDBServer(ConnectionException):
    @staticmethod
    def evoke():
        ConsoleHelper.print_error('No specific server is defined for sql database connection!')
        exit()


class NoRelationalDBDatabase(ConnectionException):
    @staticmethod
    def evoke():
        ConsoleHelper.print_error('No specific database is defined for sql database connection!')
        exit()


class NoMSSQLServerDriver(ConnectionException):
    @staticmethod
    def evoke():
        ConsoleHelper.print_error('No driver is defined fo SQL server connection!')
        exit()
