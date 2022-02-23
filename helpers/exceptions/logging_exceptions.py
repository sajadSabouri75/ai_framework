from helpers.exceptions.base_exceptions import AIFrameworkExceptions


class LogException(AIFrameworkExceptions):
    def evoke(self):
        for logger in self._loggers:
            logger.print_error("Something went wrong with logging system, don't know what!")
            logger.flush()
        exit()  # default behavior is vital error (no fault tolerance)


class TrivialLoggingException(LogException):
    def evoke(self):
        for logger in self._loggers:
            logger.print_warning('Some trivial process went wrong!')


class VitalLoggingException(LogException):
    def evoke(self, message):
        for logger in self._loggers:
            logger.print_error('Some vital process went wrong!')
            if message != '':
                logger.print_error(message)
            logger.flush()
        exit()


class NoChatIDException(LogException):
    def evoke(self):
        for logger in self._loggers:
            logger.print_warning("No chat id is provided. Telegram logging deactivated!")


# Telegram
class NoTelegramLogModeException(LogException):
    def evoke(self):
        for logger in self._loggers:
            logger.print_warning("No mode is defined for telegram logging. Default mode of 'Telegram_Lite' is set.")


class InvalidTelegramLogModeException(LogException):
    def evoke(self):
        for logger in self._loggers:
            logger.print_error("Telegram mode is not valid.")


class InvalidChatIDException(LogException):
    def evoke(self, chat_id):
        for logger in self._loggers:
            logger.print_warning(f'Chat ID {chat_id} is not subscribed!')


class NoLevelSetException(LogException):
    def evoke(self):
        for logger in self._loggers:
            logger.print_warning(f'Python logging levels are not set. Levels set to default levels of ERROR and FATAL')


class InvalidLoggingLevel(LogException):
    def evoke(self, levels):
        for logger in self._loggers:
            logger.print_warning(f'Levels {levels} is/are not valid. This level skipped!')
