from shell import Shell
from data.connect.connections_helpers import  ConnectionsTypes


def run_test():
    my_shell = Shell()
    my_shell.generate_connection(
        connection_type=ConnectionsTypes.CSV,
        csv_address='shell.py'
    )


if __name__ == '__main__':
    run_test()

