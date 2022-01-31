from helpers.exceptions.base_exceptions import AIFrameworkExceptions
from helpers.console.printing import ConsoleHelper


class ConnectionException(AIFrameworkExceptions):
    @staticmethod
    def evoke():
        ConsoleHelper.print_exception('Something went wrong with this connection!')


class NoTypeError(ConnectionException):
    @staticmethod
    def evoke():
        ConsoleHelper.print_exception('No connection type defined!')


class NoIDError(ConnectionException):
    @staticmethod
    def evoke():
        ConsoleHelper.print_exception('No valid ID for this connection!')


class NoCSVAddress(ConnectionException):
    @staticmethod
    def evoke():
        ConsoleHelper.print_exception('No CSV file address provided!')


class WrongCSVAddress(ConnectionException):
    @staticmethod
    def evoke():
        ConsoleHelper.print_exception('CSV file address seems incorrect!')


class NoCSVType(ConnectionException):
    @staticmethod
    def evoke():
        ConsoleHelper.print_exception('The specified file is not CSV.')
