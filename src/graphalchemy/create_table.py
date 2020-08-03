from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from src.graphalchemy.db_engine import db_engine
meta=MetaData()


def create_weighted_table_structure():
    weighted = Table(
        'weighted', meta,
        Column('id', String, primary_key=True),
        Column('vertex', String),
        Column('connected_to', String),
        Column('weight', Integer)
    )
    return weighted


def create_weighted_table():
    engine = db_engine()
    meta.create_all(create_weighted_table_structure(), engine)


# Base = declarative_base()
#
#
# class weighted(Base):
#     __tablename__ = 'weighted'
#
#     id = Column(String, primary_key=True)
#     vertex = Column(String)
#     connected_to = Column(String)
#     weight = Column(Integer)
#
#     def __repr__(self):
#         return "<User(name='%s', fullname='%s', nickname='%s')>" % (self.name, self.fullname, self.nickname)


if __name__ == '__main__':
    create_weighted_table()