from shell import AIShell
from data.connect.connections_helpers import ConnectionsTypes
from data.access.frame.frame_helpers import ConversionTypes
from shell_helpers import TelegramLogTypes


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
        csv_address='btc_15m_01.csv'
    )

    # shell.generate_connection(
    #     connection_type=ConnectionsTypes.SQL_SERVER,
    #     username='',
    #     password='Ssaabjoaudri@1996',
    #     server='localhost',
    #     database='my_database',
    #     driver='ODBC Driver 17 for SQL Server',
    # )

    shell.generate_connection(
        connection_type=ConnectionsTypes.MY_SQL,
        username='sajad',
        password='ss2556',
        server='localhost',  # 99.88.70.54
        database='test_for_ai',
        port='3306'
    )

    shell.generate_connection(
        connection_name='my_np',
        connection_type=ConnectionsTypes.NUMPY,
        numpy_address='test.npy'
    )

    # shell.generate_connection(
    #     connection_name='my_pickle',
    #     connection_type=ConnectionsTypes.PICKLE,
    #     pickle_address='test.pkl'
    # )


def test_get_data(shell):
    data = []

    data.append(
        shell.get_data(
            connection_name='csv',
            get_query='sdf'
        )
    )
    # data.append(
    #     shell.get_data(
    #         connection_name='rds',
    #         get_query=[{'get': 'name'}, {'get': 'profession'}, {'set': ['age', 21]}, {'get': 'blahblah'}]
    #     )
    # )
    # data.append(
    #     shell.get_data(
    #         connection_id=3,
    #         get_query=['SELECT * FROM test_table']
    #     )
    # )
    # data.append(
    #     shell.get_data(
    #         connection_name='rds',
    #         get_query=[{'get': 'name'}, {'get': 'profession'}, {'set': ['age', 21]}]
    #     )
    # )
    return data


def test_frame_data(shell, data_cache):
    framed_data = []
    for datum in data_cache:
        framed_data.append(
            shell.frame_data(
                datum,
                ConversionTypes.Spark_Dataframe
            )
        )
    return framed_data


def run_test():
    print('> Generating AI shell ...')
    my_shell = AIShell(
        name='shell_01',
        log_events=True,
    )

    # my_shell.set_telegram_logger(
    #     chat_ids=['1', '2'],
    #     mode=TelegramLogTypes.Telegram_Lite
    # )

    my_shell.set_python_logger()

    # connection generation
    print('> Generating connection ...')
    test_generate_connection(my_shell)

    # get data
    print('> Accessing data ...')
    data_cache = test_get_data(my_shell)

    # printing cached data
    print('> Cached data:')
    for datum in data_cache:
        print(datum)

    # framing data
    print('> Framing data')
    framed_data = test_frame_data(my_shell, data_cache)

    # calling it off
    print('done!')


if __name__ == '__main__':
    run_test()
