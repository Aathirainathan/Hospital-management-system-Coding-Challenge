import pyodbc
import os
import sys
from util.db_property_util import get_property_string

class DBConnUtil:
    connection = None

    @staticmethod
    def get_connection():
        if DBConnUtil.connection is None:
            connection_string = get_property_string()
            print(f"Connection String: {connection_string}")  # Print the connection string
            try:
                DBConnUtil.connection = pyodbc.connect(connection_string)
                print("Connected Successfully")
            except Exception as e:
                print("Connection failed:", e)
        return DBConnUtil.connection
