from shell import AIShell
from data.connect.connections_helpers import ConnectionsTypes


def test_generate_connection(shell):
    shell.generate_connection(
        connection_name='rds',
        connection_type=ConnectionsTypes.REDIS,
        password='',
        host='localhost',
        port='6380',
        database_index=0
    )

    shell.generate_connection(
        connection_type=ConnectionsTypes.CSV,
        connection_name='csv',
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

    shell.generate_connection(
        connection_type=ConnectionsTypes.MY_SQL,
        username='sajad',
        password='ss2556',
        server='localhost', # 99.88.70.54
        database='test_for_ai',
        port='3306'
    )

    shell.generate_connection(
        connection_name='my_np',
        connection_type=ConnectionsTypes.NUMPY,
        numpy_address='test.npy'
    )

    shell.generate_connection(
        connection_name='my_pickle',
        connection_type=ConnectionsTypes.PICKLE,
        pickle_address='test.pkl'
    )


def test_get_data(shell):
    # shell.get_data(
    #     connection_name='rds'
    # )
    data = shell.get_data(
        connection_name='csv',
        get_query='sdf'
    )
    data = shell.get_data(
        connection_name='rds',
        get_query=[{'get': 'name'}, {'get': 'profession'}, {'set': ['age', 21]}]
    )
    data = shell.get_data(
        connection_id=3,
        get_query=['SELECT * FROM test_table']
    )
    return data


def run_test():
    my_shell = AIShell(name='shell_01')
    test_generate_connection(my_shell)
    last_data = test_get_data(my_shell)
    print(last_data)

    # calling it off
    print('done!')


if __name__ == '__main__':
    run_test()

