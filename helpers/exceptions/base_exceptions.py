

class AIFrameworkExceptions(Exception):
    pass


class NoException(Exception):
    @staticmethod
    def evoke():
        pass