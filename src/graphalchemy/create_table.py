from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy.orm import sessionmaker

from src.graphalchemy.read_dbcfg import read_config
from src.graphalchemy.db_engine import db_engine
import pandas as pd
from pathlib import Path


def weighted_table():
    """
    Create and insert data into weighted table
    """
    engine = db_engine()
    meta = MetaData(engine)
    config = read_config()
    weighted = Table(
        config['database']['postgres']['table']['weighted'], meta,
        Column('id', Integer, primary_key=True),
        Column('vertex', String),
        Column('connection', String),
        Column('weight', Integer)
    )
    try:
        weighted.create()
        try:
            data = pd.read_csv(str(Path.home()) + '/.etc/data/weighted.csv')
            print(data)
            data.to_sql(config['database']['postgres']['table']['weighted'], engine, if_exists='replace', index = False)
            # Session = sessionmaker(bind=engine.connect())
            # session = Session()
            # session.bulk_insert_mappings(weighted, data.to_dict(orient="records"))
            # session.close()
            return 'successfully created and inserted data into weighted table'
        except BaseException:
            return 'error inserting data into weighted table'
    except BaseException:
        return 'error creating weighted table'


def directed_table():
    """
    Create and insert data into the directed table
    """
    engine = db_engine()
    meta = MetaData(engine)
    config = read_config()
    directed = Table(
        config['database']['postgres']['table']['directed'], meta,
        Column('id', String, primary_key=True),
        Column('vertex', String),
        Column('connection', String),
        Column('weight', Integer)
    )
    try:
        directed.create()
        try:
            data = pd.read_csv(str(Path.home()) + '/.etc/data/directed.csv')
            data.to_sql(config['database']['postgres']['table']['directed'], engine, if_exists='replace', index=False)
            # Session = sessionmaker(bind=engine.connect())
            # session = Session()
            # session.bulk_insert_mappings(directed, data.to_dict(orient="records"))
            # session.close()
            return 'successfully created and inserted data into directed table'
        except BaseException:
            return 'error inserting data into directed table'
    except BaseException:
        return 'error creating directed table'


if __name__ == '__main__':
    print(weighted_table())
    print(directed_table())