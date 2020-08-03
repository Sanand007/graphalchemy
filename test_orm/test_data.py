import sqlalchemy as db
from src.graphalchemy.db_engine import db_engine
from src.graphalchemy.read_dbcfg import read_config


def test_data_weighted():
    """
    test the size of data in weighted table i.e., 6
    """
    engine = db_engine()
    config = read_config()
    weighted_table = db.Table(config['database']['postgres']['table']['weighted'], db.MetaData(), autoload=True, autoload_with=engine)
    query = db.select([weighted_table])
    ResultProxy = engine.connect().execute(query)
    data = ResultProxy.fetchall()
    assert len(data) == 6
