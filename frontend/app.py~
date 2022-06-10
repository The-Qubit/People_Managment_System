#!/usr/bin/env python3

from flask import Flask, request
from flask import request
import sqlite3

app = Flask(__name__)

def gen_data():
    connection = sqlite3.connect('../backend/Profiles.db')
    cursor = connection.cursor()
    cursor.execute('SELECT id, fname, lname FROM person;')
    results = cursor.fetchall()
    data = ''
    for result in results:
        data += '<tr>\n'
        data += '\n'.join(['<td>' + str(attr) + '</td>' for attr in result])
        data += '</tr>\n'
    return data

def add_profile(fname, lname):
    connection = sqlite3.connect('../backend/Profiles.db')
    cursor = connection.cursor()
    cursor.execute('SELECT id, fname, lname FROM person ORDER BY id DESC LIMIT 1;')
    results = cursor.fetchall()
    id_ = -1
    for result in results:
        id_ = result[0]
    id_ += 1
    cursor.execute(f'INSERT INTO person (id,fname,lname) VALUES ({id_},"{fname}","{lname}");')

@app.route("/")
def root():
    fname = request.args.get('fname')
    lname = request.args.get('lname')

    if fname:
        add_profile(fname, lname)

    html = open('index.html').read()
    data = gen_data()
    html = html.replace("{{ data }}", data)

    return html

