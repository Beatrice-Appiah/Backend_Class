# Low level library
from sqlalchemy import create_engine #to connect our database to sqlalchemy
# It acts as a bridge between our pyhton appp and database informs sqlalchemy how to connect to our database including, location of database, credentials needed to access the database
# High level library
from sqlalchemy.orm import sessionmaker
# Session is a workspace where we can do operations like add, update, delete

connection_str = 'mysql+mysqlconnector://username:password@localhost/tech4girls'

engine = create_engine(connection_str)

try:
    connection = engine.connect() # .connect()establishes an active connection to our dtabase
    print('Located and connected to database')
    # After opening it is best to close it
    connection.close()
except Exception as e:
    print(f'An error occured: {e}')

DBSession = sessionmaker(bind = engine)
session = DBSession()