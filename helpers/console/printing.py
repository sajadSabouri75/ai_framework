from colorama import Fore


class ConsoleHelper():

    @staticmethod
    def define_framework():
        print(f'>> {Fore.LIGHTBLUE_EX}AI Framework running{Fore.RESET}')

    @staticmethod
    def define_connection(tag, connection_id):
        if tag == 'start':
            print(f'{Fore.BLUE}<connection_{connection_id}>{Fore.RESET}')
        elif tag == 'end':
            print(f'{Fore.BLUE}</connection_{connection_id}>{Fore.RESET}')

    @staticmethod
    def print_warning(warning_message):
        print(f'<warning> {Fore.LIGHTYELLOW_EX}{warning_message}{Fore.RESET} </warning>')

    @staticmethod
    def print_error(error_message):
        print(f'<error> {Fore.LIGHTRED_EX} {error_message} {Fore.RESET}</error>')

    @staticmethod
    def confirm_connection(connection_id):
        print(f'<confirmation> {Fore.LIGHTGREEN_EX}connection {connection_id} confirmed!{Fore.RESET} </confirmation>')

    @staticmethod
    def print_internal_message(message):
        print(f'<message> {Fore.LIGHTWHITE_EX}{message}{Fore.RESET}</message>')