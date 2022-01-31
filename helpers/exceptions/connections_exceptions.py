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
