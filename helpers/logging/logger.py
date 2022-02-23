

class Logger:
    def __init__(self, **kwargs):
        self._loggers = kwargs['loggers'] if 'loggers' in kwargs else None
