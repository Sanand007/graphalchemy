import sqlalchemy as db
from src.graphalchemy.db_engine import db_engine


def _read_weighted_data(table_name) -> list:
    try:
        engine = db_engine()
        weighted_table = db.Table('weighted', db.MetaData(), autoload=True, autoload_with=engine)
        query = db.select([weighted_table])
        ResultProxy = engine.connect().execute(query)
        data = ResultProxy.fetchall()
        return data
    except BaseException:
        return None


def read_weighted_data(table_name) -> list:
    """
    takes table_name as input and returns list as output
    read weighted data from database and return a list containing data
    """
    return _read_weighted_data(table_name)


def _read_directed_data(table_name) -> list:
    try:
        engine = db_engine()
        weighted_table = db.Table(table_name, db.MetaData(), autoload=True, autoload_with=engine)
        query = db.select([weighted_table])
        ResultProxy = engine.connect().execute(query)
        data = ResultProxy.fetchall()
        return data
    except BaseException:
        return None


def read_directed_data(table_name) -> list:
    """
    read directed data from database and return a list containing data
    """
    return _read_directed_data(table_name)