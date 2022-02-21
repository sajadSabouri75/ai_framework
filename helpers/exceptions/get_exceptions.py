from helpers.exceptions.base_exceptions import AIFrameworkExceptions
from helpers.console.printing import ConsoleHelper


class GetException(AIFrameworkExceptions):
    @staticmethod
    def evoke():
        ConsoleHelper.print_error("Something went wrong with this connection, don't know what!")
        exit() # default behavior is vital error (no fault tolerance)


class TrivialGetException(GetException):
    @staticmethod
    def evoke():
        ConsoleHelper.print_warning('Some trivial process went wrong!')


class VitalGetException(GetException):
    @staticmethod
    def evoke():
        ConsoleHelper.print_error('Some vital process went wrong!')
        exit()


class NoIdentification(GetException):
    @staticmethod
    def evoke():
        ConsoleHelper.print_error('No connection identification is defined! Please insert connection id or name!')
        exit()


class InvalidID(GetException):
    @staticmethod
    def evoke():
        ConsoleHelper.print_error('Connection id is not found!')
        exit()


class InvalidName(GetException):
    @staticmethod
    def evoke():
        ConsoleHelper.print_error('Connection name is not found!')
        exit()


class InvalidNameIDPair(GetException):
    @staticmethod
    def evoke():
        ConsoleHelper.print_error('Connection name and id do not pair!')
        exit()


class RedundantCSVQuery(GetException):
    @staticmethod
    def evoke():
        ConsoleHelper.print_warning('CSV files do not accept queries. Query ignored!')


class NoGetQuery(GetException):
    @staticmethod
    def evoke():
        ConsoleHelper.print_error('No query is defined for data retrieval!')