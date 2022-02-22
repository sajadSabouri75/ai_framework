from helpers.exceptions.base_exceptions import AIFrameworkExceptions
from helpers.logging.console_broadcast import ConsoleBroadcast


class FrameException(AIFrameworkExceptions):
    @staticmethod
    def evoke():
        ConsoleBroadcast.print_error("Something went wrong with this connection, don't know what!")
        exit() # default behavior is vital error (no fault tolerance)


class TrivialFrameException(FrameException):
    @staticmethod
    def evoke():
        ConsoleBroadcast.print_warning('Some trivial process went wrong!')


class VitalFrameException(FrameException):
    @staticmethod
    def evoke(message=''):
        ConsoleBroadcast.print_error('Some vital process went wrong!')
        if message != '':
            ConsoleBroadcast.print_error(message)

        exit()


# Pandas -> RDD | Spark
class NoPandasObject(FrameException):
    @staticmethod
    def evoke():
        ConsoleBroadcast.print_error('For this conversion, an input of type "pandas dataframe" is required!')


class NoPandasType(FrameException):
    @staticmethod
    def evoke():
        ConsoleBroadcast.print_error('Input file is not of type "pandas dataframe"')


