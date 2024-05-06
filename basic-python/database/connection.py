import sqlite3
from sqlite3 import Error


class DatabaseConnection:
    def __init__(self, database_file):
        self.conn = None
        try:
            self.conn = sqlite3.connect(database_file)
            print("Connection to DB successful")
        except Error as e:
            print(e)

    def close_connection(self):
        self.conn.close()

    def create_table(self, create_table_sql):
        try:
            c = self.conn.cursor()
            c.execute(create_table_sql)
        except Error as e:
            print(e)

    def get_cursor(self):
        return self.conn.cursor()

    def get_connection(self):
        return self.conn
