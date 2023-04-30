#!/usr/bin/env python3

import sys

import pyodbc

def main():
    server = '192.168.178.24:1433'
    database = 'master'
    username = 'sa'
    password = 'Survive_Hertz_Massager_Rage_Creative_Grievous_Mossy_Purify144!'

    conn = pyodbc.connect(f'''
      DRIVER={{ODBC Driver 18 for SQL Server}};
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
