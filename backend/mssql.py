import os

import pyodbc

def get_connection():
    driver = '{ODBC Driver 17 for SQL Server}'
    server = '192.168.178.24,1433'
    # server = 'host.docker.internal,1433'
    database = 'users'
    username = 'sa'
    password = os.environ.get('DB_PASSWORD')

    return pyodbc.connect(
      driver=driver,
      host=server,
      database=database,
      user=username,
      password=password,
    )

def get_all_users():
    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(f'SELECT email, password FROM users;')

    # conn.commit()

    results = list(map(tuple, cursor.fetchall()))

    conn.close()

    return results
