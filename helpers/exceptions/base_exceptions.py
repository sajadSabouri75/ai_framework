from helpers.logging.console_broadcast import ConsoleBroadcast


class AIFrameworkExceptions(Exception):
    pass


class NoException(Exception):
    @staticmethod
    def evoke():
        pass


class VitalException(AIFrameworkExceptions):
    @staticmethod
    def evoke(message=''):
        ConsoleBroadcast.print_error('Some vital process went wrong!')
        if message != '':
            ConsoleBroadcast.print_error(message)
        exit()
