from shell import AIShell
from data.connect.connections_helpers import ConnectionsTypes


def test_generate_connection(shell):
    shell.generate_connection(
        connection_name='rds',
        connection_type=ConnectionsTypes.REDIS,
        password='',
        host='localhost',
        port='6379',
        database_index=0
    )

    shell.generate_connection(
        connection_type=ConnectionsTypes.CSV,
        csv_address='test.csv'
    )

    # shell.generate_connection(
    #     connection_type=ConnectionsTypes.SQL_SERVER,
    #     username='admin',
    #     password='1234',
    #     server='180.0.0.100',
    #     database='my_database',
    #     driver='ODBC Driver 17 for SQL Server',
    # )

    # shell.generate_connection(
    #     connection_type=ConnectionsTypes.MY_SQL,
    #     username='admin',
    #     password='1234',
    #     server='180.0.0.100',
    #     database='my_database',
    #     driver='ODBC Driver 17 for SQL Server',
    # )

    # shell.generate_connection(
    #     connection_type=ConnectionsTypes.REDIS,
    #     password='',
    #     host='localhost',
    #     port='3679'
    # )


def test_get_data(shell):
    shell.get_data(
        connection_name='rds'
    )


def run_test():
    my_shell = AIShell()
    test_generate_connection(my_shell)
    test_get_data(my_shell)


if __name__ == '__main__':
    run_test()

