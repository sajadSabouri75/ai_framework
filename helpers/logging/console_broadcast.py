from colorama import Fore
from helpers.logging.logger import Logger


class ConsoleBroadcast(Logger):

    @staticmethod
    def define_framework():
        print(f'>> {Fore.LIGHTBLUE_EX}AI Framework running{Fore.RESET}')

    @staticmethod
    def define_connection(tag):
        if tag == 'start':
            print(f'{Fore.BLUE}<connection>{Fore.RESET}')
        elif tag == 'end':
            print(f'{Fore.BLUE}</connection>{Fore.RESET}')

    @staticmethod
    def print_warning(warning_message):
        print(f'<warning> {Fore.LIGHTYELLOW_EX}{warning_message}{Fore.RESET} </warning>')

    @staticmethod
    def print_error(error_message):
        print(f'<error> {Fore.LIGHTRED_EX} {error_message} {Fore.RESET}</error>')

    @staticmethod
    def confirm_connection(connection_id, connection_name):
        print(
            f'<connection_confirmation> '
            f'{Fore.LIGHTGREEN_EX}connection [{connection_id}:{connection_name}] confirmed!{Fore.RESET} '
            f'</connection_confirmation>'
        )

    @staticmethod
    def print_internal_message(message):
        print(f'<message> {Fore.LIGHTWHITE_EX}{message}{Fore.RESET}</message>')

    @staticmethod
    def define_get(tag):
        if tag == 'start':
            print(f'{Fore.BLUE}<get>{Fore.RESET}')
        elif tag == 'end':
            print(f'{Fore.BLUE}</get>{Fore.RESET}')

    @staticmethod
    def confirm_data_cache(connection_id, connection_name):
        print(
            f'<data_cache> '
            f'{Fore.LIGHTGREEN_EX}data from connection [{connection_id}:{connection_name}] cached!{Fore.RESET} '
            f'</data_cache>'
        )

    @staticmethod
    def define_frame(tag):
        if tag == 'start':
            print(f'{Fore.BLUE}<frame>{Fore.RESET}')
        elif tag == 'end':
            print(f'{Fore.BLUE}</frame>{Fore.RESET}')

    @staticmethod
    def confirm_framing():
        print(
            f'<frame_confirmation> '
            f'{Fore.LIGHTGREEN_EX}framed successfully!{Fore.RESET} '
            f'</frame_confirmation>'
        )

    @staticmethod
    def flush():
        pass



