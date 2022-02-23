

class Get:
    def __init__(self, **kwargs):
        self._connection_obj = kwargs['connection_obj'] if 'connection_obj' in kwargs else None
        self._loggers = kwargs['loggers'] if 'loggers' in kwargs else []
        self._cache = []
