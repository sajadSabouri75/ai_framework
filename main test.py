from shell import AIShell
from data.connect.connections_helpers import  ConnectionsTypes


def run_test():
    my_shell = AIShell()
    my_shell.generate_connection(
        connection_type=ConnectionsTypes.CSV,
        csv_address='test.csv'
    )


if __name__ == '__main__':
    run_test()

