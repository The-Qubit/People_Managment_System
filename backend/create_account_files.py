#!/usr/bin/env python3

import sys
import os
from consts import db_dir, default_profile_attrs

def create_profile_csv(username='maxmustermann'):
    global db_dir
    try:
        with open(os.path.join(db_dir, username, 'profile.csv'), 'w') as f:
            f.write(default_profile_attrs)
    except Exception as e:
        print('An error occured')
        print(e)

def create_account_folder(username='maxmustermann'):
    global db_dir
    try:
        os.mkdir(os.path.join(db_dir))
    except FileExistsError:
        pass
    try:
        os.mkdir(os.path.join(db_dir, username))
    except FileExistsError:
        print('A user with that username already exists')

if __name__ == '__main__':
    if len(sys.argv) == 2:
        username = sys.argv[1]
        create_account_folder(username)
        create_profile_csv(username)
    else:
        print('Error: Scripts must be run with 1 parameter')
        sys.exit(1)
