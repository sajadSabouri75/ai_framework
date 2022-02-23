import logging
from colorama import Fore
from helpers.exceptions import logging_exceptions as excepts
from helpers.logging.logger import Logger


VALID_LEVELS = ['INFO', 'WARNING', 'ERROR', 'FATAL']


class PythonLogging(Logger):
    def __init__(self, **kwargs):
        super(PythonLogging, self).__init__(**kwargs)
        self._loggers = kwargs['loggers'] if 'loggers' in kwargs else []
        self._levels = kwargs['levels'] if 'levels' in kwargs else []
        if self._levels is not None:
            self._levels = [str(level).upper() for level in self._levels]
        self.check_on_construction_inputs()

    def check_on_construction_inputs(self):
        try:
            if self._levels is None:
                self._levels = ['FATAL', 'ERROR']
                raise excepts.NoLevelSetException(self._loggers)
            invalid_levels = []
            for level in self._levels:
                if level not in VALID_LEVELS:
                    invalid_levels.append(level)
            if len(invalid_levels) > 0:
                raise excepts.InvalidLoggingLevel(self._loggers)

        except excepts.InvalidLoggingLevel as e:
            e.evoke(invalid_levels)
        except excepts.LogException as e:
            e.evoke()
        except Exception as e:
            excepts.VitalLoggingException(self._loggers).evoke(e)

    def define_framework(self):
        if 'INFO' in self._levels:
            logging.info(f'>> {Fore.LIGHTBLUE_EX}AI Framework running{Fore.RESET}')

    def define_connection(self, tag):
        if 'INFO' in self._levels:
            if tag == 'start':
                logging.info(f'{Fore.BLUE}<connection>{Fore.RESET}')
            elif tag == 'end':
                logging.info(f'{Fore.BLUE}</connection>{Fore.RESET}')

    def print_warning(self, warning_message):
        if 'WARNING' in self._levels:
            logging.warning(f'<warning> {Fore.LIGHTYELLOW_EX}{warning_message}{Fore.RESET} </warning>')

    def print_error(self, error_message):
        if 'ERROR' in self._levels:
            logging.error(f'<error> {Fore.LIGHTRED_EX} {error_message} {Fore.RESET}</error>')

    def confirm_connection(self, connection_id, connection_name):
        if 'INFO' in self._levels:
            logging.info(
                f'<connection_confirmation> '
                f'{Fore.LIGHTGREEN_EX}connection [{connection_id}:{connection_name}] confirmed!{Fore.RESET} '
                f'</connection_confirmation>'
            )

    def print_internal_message(self, message):
        if 'INFO' in self._levels:
            logging.info(f'<message> {Fore.LIGHTWHITE_EX}{message}{Fore.RESET}</message>')

    def define_get(self, tag):
        if 'INFO' in self._levels:
            if tag == 'start':
                logging.info(f'{Fore.BLUE}<get>{Fore.RESET}')
            elif tag == 'end':
                logging.info(f'{Fore.BLUE}</get>{Fore.RESET}')

    def confirm_data_cache(self, connection_id, connection_name):
        if 'INFO' in self._levels:
            logging.info(
                f'<data_cache> '
                f'{Fore.LIGHTGREEN_EX}data from connection [{connection_id}:{connection_name}] cached!{Fore.RESET} '
                f'</data_cache>'
            )

    def define_frame(self, tag):
        if 'INFO' in self._levels:
            if tag == 'start':
                logging.info(f'{Fore.BLUE}<frame>{Fore.RESET}')
            elif tag == 'end':
                logging.info(f'{Fore.BLUE}</frame>{Fore.RESET}')

    def confirm_framing(self):
        if 'INFO' in self._levels:
            logging.info(
                f'<frame_confirmation> '
                f'{Fore.LIGHTGREEN_EX}framed successfully!{Fore.RESET} '
                f'</frame_confirmation>'
            )

    def flush(self):
        pass



