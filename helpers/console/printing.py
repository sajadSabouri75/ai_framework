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
    def print_exception(error_message):
        print(f'{Fore.RED}AI-Framework ERROR> {error_message}{Fore.RESET}')