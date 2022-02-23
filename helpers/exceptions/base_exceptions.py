from helpers.logging.console_broadcast import ConsoleBroadcast


class AIFrameworkExceptions(Exception):
    def __init__(self, loggers):
        self._loggers = loggers
    pass


class NoException(Exception):
    def evoke(self):
        pass


class VitalException(AIFrameworkExceptions):
    def evoke(self, message=''):
        for logger in self._loggers:
            logger.print_error('Some vital process went wrong!')
            if message != '':
                logger.print_error(message)
            logger.flush()
        exit()
