from colorama import Fore


class ConsoleHelper():

    @staticmethod
    def define_framework():
        print(f'>> {Fore.LIGHTBLUE_EX}AI Framework running{Fore.RESET}')

    @staticmethod
    def define_connection(tag, connection_id):
        if tag == 'start':
            print(f'{Fore.BLUE}<connections_{connection_id}>{Fore.RESET}')
        elif tag == 'end':
            print(f'{Fore.BLUE}</connections_{connection_id}>{Fore.RESET}')

    @staticmethod
    def print_warning(warning_message):
        print(f'{Fore.YELLOW}<WARNING> {warning_message} </WARNING>{Fore.RESET}')

    @staticmethod
    def print_error(error_message):
        print(f'{Fore.RED}<ERROR> {error_message} </ERROR>')

    @staticmethod
    def confirm_connection(connection_id):
        print(f'{Fore.GREEN}connection {connection_id} confirmed!{Fore.RESET}')