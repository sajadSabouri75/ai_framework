from helpers.exceptions.base_exceptions import AIFrameworkExceptions
from helpers.logging.console_broadcast import ConsoleBroadcast


class FrameException(AIFrameworkExceptions):
    def evoke(self):
        for logger in self._loggers:
            logger.print_error("Something went wrong with this connection, don't know what!")
            logger.flush()
        exit()  # default behavior is vital error (no fault tolerance)


class TrivialFrameException(FrameException):
    def evoke(self):
        for logger in self._loggers:
            logger.print_warning('Some trivial process went wrong!')


class VitalFrameException(FrameException):
    def evoke(self, message=''):
        for logger in self._loggers:
            logger.print_error('Some vital process went wrong!')
            if message != '':
                logger.print_error(message)
            logger.flush()
        exit()


# Pandas -> RDD | Spark
class NoPandasObject(FrameException):
    def evoke(self):
        for logger in self._loggers:
            logger.print_error('For this conversion, an input of type "pandas dataframe" is required!')
            logger.flush()
        exit()


class NoPandasType(FrameException):
    def evoke(self):
        for logger in self._loggers:
            logger.print_error('Input file is not of type "pandas dataframe"')
            logger.flush()
        exit()

