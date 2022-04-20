
import mysql.connector as sql
from mysql.connector import errorcode, Error

def connect_to_database(host, database, user, password):
    """Make connection to the DB and return connection object and cursor """

    try:
        connection = sql.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )
        if connection.is_connected():
            print(f"Connected to {database!r} DB")
            cursor = connection.cursor()
            return connection, cursor

    except Error as e:
        if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif e.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print("Error while connecting to the DB: ", e)
    else:
        connection.close()