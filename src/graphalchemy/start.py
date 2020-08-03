import sqlalchemy as db
from src.graphalchemy.db_engine import database_engine
from src.graphalchemy.read_dbcfg import database_config
import pandas as pd
import psycopg2


def read_data():
    engine = database_engine()
    con = psycopg2.connect("host='localhost' dbname='galchemy' user='juhi' password='1234'")
    cur = con.cursor()
    cur.execute("SELECT * FROM galchemy.weighted")
    while True:
        row = cur.fetchone()

        if row == None:
            break

        print("Product: " + row[1] + "\t\tPrice: " + str(row[2]))

    config = database_config()
    weighted_table = db.Table('weighted', db.MetaData(), autoload=True, autoload_with=engine)
    query = db.select([weighted_table])
    ResultProxy = engine.connect().execute(query)
    data = ResultProxy.fetchall()
    print(type(data))


if __name__ == '__main__':
    read_data()