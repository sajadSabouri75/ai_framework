from shell import AIShell
from data.connect.connections_helpers import ConnectionsTypes


def run_test():

    my_shell = AIShell()

    my_shell.generate_connection(
        connection_type=ConnectionsTypes.REDIS,
        password='',
        host='localhost',
        port='3679'
    )

    my_shell.generate_connection(
        connection_type=ConnectionsTypes.CSV,
        csv_address='test.csv'
    )

    # my_shell.generate_connection(
    #     connection_type=ConnectionsTypes.SQL_SERVER,
    #     username='admin',
    #     password='1234',
    #     server='180.0.0.100',
    #     database='my_database',
    #     driver='ODBC Driver 17 for SQL Server',
    # )

    my_shell.generate_connection(
        connection_type=ConnectionsTypes.MY_SQL,
        username='admin',
        password='1234',
        server='180.0.0.100',
        database='my_database',
        driver='ODBC Driver 17 for SQL Server',
    )

    my_shell.generate_connection(
        connection_type=ConnectionsTypes.REDIS,
        password='',
        host='localhost',
        port='3679'
    )


if __name__ == '__main__':
    run_test()

