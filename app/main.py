import sys
import csv
from time import time
from sqlalchemy import Column, Integer, Float, Date, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


db_name = 'database'
db_user = 'test1234'
db_pass = '1234'
db_host = 'db'
db_port = '5432'


db_string = f'postgresql://{db_user}:{db_pass}@{db_host}/{db_name}'
db = create_engine(db_string)

# inputs loaded as list starting with index 0
# Future enhancement to pass in File name, Coin name, and Ticker in the CMD calls instead of hardcoded in Main()
inputs = sys.argv[1:]
base = declarative_base()


class PriceHistory(base):
    __tablename__ = "price_history"
    price_history_id = Column(Integer, primary_key=True)
    ticker = Column(String)
    coin_name = Column(String)
    price_dt = Column(Date)
    open = Column(Float)
    high = Column(Float)
    low = Column(Float)
    close = Column(Float)
    volume = Column(Float)
    currency = Column(String)


def csv_read(file_name):
    """
    Reads from the specified csv file passed in and adds the records for it to a list
    """
    li = []
    with open(file_name, newline='') as csvfile:
        file_reader = csv.reader(csvfile, delimiter=',')
        next(file_reader, None)
        for row in file_reader:
            li.append(row)
    return li


def transformation(file_name, coin_name, ticker):
    """
    Used to load data to the table. A session is first configured to establish a session with the
    database. Function csv_read() is called passing in the current file name. For each record returned 
    in the list from csv_read() they are mapped to the corresponding columns from PriceHistory class.
    A row is added to the table on each loop and finally committed to the DB once all records are read.
    The columnd prices_key is a sequence generated column on the table.
    """

    t = time()

    session = sessionmaker()
    session.configure(bind=db)
    s = session()

    try:
        file_name = f"{file_name}.csv"
        path = '/data/' + file_name
        print("file name is ", path)
        data = csv_read(path)

        for rec in data:
            record = PriceHistory(**{
                'price_history_id': None,
                'ticker': ticker,
                'coin_name': coin_name,
                'price_dt': rec[0],
                'open': rec[1],
                'high': rec[2],
                'low': rec[3],
                'close': rec[4],
                'volume': rec[5],
                'currency': rec[6]
            })
            s.add(record)
        s.commit()
    except:
        print('error rolling back')
        s.rollback()
    finally:
        s.close()
    print("Time elapsed: " + str(time() - t) + " s.")


def main():
    """
    Calls to transformation() to load 5 files sequentially at the moment
    """
    # transformation(inputs[0], inputs[1], inputs[2])
    print('------------------------------------------------')
    print('---------------Execution Starting---------------')
    print('------------------------------------------------')
    transformation('Solana', 'Solana', 'SOL')
    transformation('Bitcoin', 'Bitcoin', 'BTC')
    transformation('Ethereum', 'Ethereum', 'ETH')
    transformation('Aave', 'Aave', 'AAVE')
    transformation('Zcash', 'Zcash', 'ZEC')
    print('------------------------------------------------')
    print('---------------Execution Complete---------------')
    print('------------------------------------------------')


if __name__ == "__main__":
    main()
