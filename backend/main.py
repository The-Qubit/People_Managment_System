#!/usr/bin/env python3

import sys

import pyodbc

def main():
    server = 'localhost:1433'
    database = 'master'
    username = 'sa'
    password = 'User Retrain Shelve Showy Goatskin Dowry Twelve Petunia'

    conn = pyodbc.connect(f'''
      DRIVER={{ODBC Driver 17 for SQL Server}};
      SERVER={server};
      DATABASE={database};
      UID={username};
      PWD={password}'''
    )

    new_db_name = 'test'
    cursor.execute(f'CREATE DATABASE {new_db_name}')

    conn.commit()

    conn.close()

if __name__ == '__main__':
    sys.exit(main())
