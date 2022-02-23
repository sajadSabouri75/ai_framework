from helpers.exceptions.base_exceptions import AIFrameworkExceptions
from helpers.logging.console_broadcast import ConsoleBroadcast


class GetException(AIFrameworkExceptions):
    def evoke(self):
        for logger in self._loggers:
            logger.print_error("Something went wrong with this get, don't know what!")
            logger.flush()
        exit()  # default behavior is vital error (zero fault tolerance)


class TrivialGetException(GetException):
    def evoke(self):
        for logger in self._loggers:
            logger.print_warning('Some trivial process went wrong!')


class VitalGetException(GetException):
    def evoke(self, message=''):
        for logger in self._loggers:
            logger.print_error('Some vital process went wrong!')
            if message != '':
                logger.print_error(message)
            logger.flush()

        exit()


class NoIdentification(GetException):
    def evoke(self):
        for logger in self._loggers:
            logger.print_error('No connection identification is defined! Please insert connection id or name!')
            logger.flush()
        exit()


class InvalidID(GetException):
    def evoke(self):
        for logger in self._loggers:
            logger.print_error('Connection id is not found!')
            logger.flush()
        exit()


class InvalidName(GetException):
    def evoke(self):
        for logger in self._loggers:
            logger.print_error('Connection name is not found!')
            logger.flush()
        exit()


class InvalidNameIDPair(GetException):
    def evoke(self):
        for logger in self._loggers:
            logger.print_error('Connection name and id do not pair!')
            logger.flush()
        exit()


class RedundantCSVQuery(GetException):
    def evoke(self):
        for logger in self._loggers:
            logger.print_warning('CSV files do not accept queries. Query ignored!')


class NoGetQuery(GetException):
    def evoke(self):
        for logger in self._loggers:
            logger.print_error('No query is defined for data retrieval!')
            logger.flush()
        exit()


class EmptyQueryResult(GetException):
    def evoke(self, query):
        for logger in self._loggers:
            logger.print_warning(f'The specified query [{query}] resulted in empty result set!')
            logger.flush()
        exit()
