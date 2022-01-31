from colorama import Fore


class ConsoleHelper():

    @staticmethod
    def define_framework():
        print(f'>> {Fore.LIGHTBLUE_EX}AI Framework running{Fore.RESET}')

    @staticmethod
    def define_connection(tag):
        if tag == 'start':
            print(f'{Fore.BLUE}<connections>{Fore.RESET}')
        elif tag == 'end':
            print(f'{Fore.BLUE}</connections>{Fore.RESET}')

    @staticmethod
    def print_warning(warning_message):
        print(f'{Fore.YELLOW}<WARNING> {warning_message} </WARNING>{Fore.RESET}')

    @staticmethod
    def print_error(error_message):
        print(f'{Fore.RED}<ERROR> {error_message} </ERROR>')
