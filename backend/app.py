#!/usr/bin/env python3

import sys

from flask import Flask, request
import mssql

app = Flask(__name__)

def get_user(email, users) -> tuple:
    for user in users:
        if email == user[0]:
            return user
    return None

@app.route('/sign_in', methods=['GET'])
def sign_in():
    email = request.args.get('email')
    password = request.args.get('password')

    user = get_user(email, mssql.get_all_users())
    if user is None:
        print(f'Email does not exist')
        return 'Bad Email\n'
    if password != user[1]:
        print(f'Email exists but wrong password')
        return 'Bad Password\n'

    print(f'Authentication successful')

    return 'OK\n'

if __name__ == '__main__':
    sys.exit(app.run(host='0.0.0.0', port=5000))
