#!/usr/bin/env python3

import sys

import pyodbc

def main():
    server = 'host.docker.internal'
    database = 'test'
    username = 'sa'
    password = 'Survive_Hertz_Massager_Rage_Creative_Grievous_Mossy_Purify144!'

    conn = pyodbc.connect(
      driver='{ODBC Driver 17 for SQL Server}',
      host=server,
      database=database,
      user=username,
      password=password,
    )

    cursor = conn.cursor()

    cursor.execute(f'SELECT * FROM test1;')

    for row in cursor.fetchall():
        print(tuple(row))

    # conn.commit()

    conn.close()

if __name__ == '__main__':
    sys.exit(main())
