from enum import Enum


class ConnectionsTypes(Enum):
    MANUAL = 0
    SQL_SERVER = 1
    MY_SQL = 2
    CSV = 3
    REDIS = 4
