

class Frame:
    def __init__(self, **kwargs):
        self._loggers = kwargs['loggers'] if 'loggers' in kwargs else []
        self._subject_type = None
        self._object_type = None
