from helpers.exceptions.base_exceptions import AIFrameworkExceptions
from helpers.logging.console_broadcast import ConsoleBroadcast


class LogException(AIFrameworkExceptions):
    @staticmethod
    def evoke():
        ConsoleBroadcast.print_error("Something went wrong with logging system, don't know what!")
        exit()  # default behavior is vital error (no fault tolerance)


class TrivialLoggingException(LogException):
    @staticmethod
    def evoke():
        ConsoleBroadcast.print_warning('Some trivial process went wrong!')


class VitalLoggingException(LogException):
    @staticmethod
    def evoke(message=''):
        ConsoleBroadcast.print_error('Some vital process went wrong!')
        if message != '':
            ConsoleBroadcast.print_error(message)

        exit()


class NoChatIDException(LogException):
    @staticmethod
    def evoke():
        ConsoleBroadcast.print_warning("No chat id is provided. Telegram logging deactivated!")


# Telegram
class NoTelegramLogModeException(LogException):
    @staticmethod
    def evoke():
        ConsoleBroadcast.print_warning(
            "No mode is defined for telegram logging. Default mode of 'Telegram_Lite' is set."
        )


class InvalidTelegramLogModeException(LogException):
    @staticmethod
    def evoke():
        ConsoleBroadcast.print_error("Telegram mode is not valid.")


class InvalidChatIDException(LogException):
    @staticmethod
    def evoke(chat_id):
        ConsoleBroadcast.print_warning(f'Chat ID {chat_id} is not subscribed!')
