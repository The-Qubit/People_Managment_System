#!/usr/bin/env python3

import sys
import os
import csv
from io import StringIO
from consts import db_dir

def add_lines_to_table(username, table, fieldnames, lines):
    file_exists = os.path.exists(os.path.join(db_dir, username, table + '.csv'))
    with open(os.path.join(db_dir, username, table + '.csv'), 'a') as table_csv:
        table_file = csv.DictWriter(table_csv, fieldnames=fieldnames, delimiter=',', quotechar='"')
        if not file_exists:
            table_file.writeheader()
        for line in lines:
            table_file.writerow(dict(line))

def create_new_profile(username, attributes_raw):
    global db_dir
    attributes = [ (attribute.split(':', 1)[0], attribute.split(':', 1)[1]) for attribute in attributes_raw ]

    with open(os.path.join(db_dir, username, 'profile.csv')) as profiles_csv:
        profiles = list(csv.reader(profiles_csv, delimiter=',', quotechar='"'))
    # Gets all rows (without first row), then gets every first element
    # (assumes that the first column is the primary key integer id) and
    # calculates the max of that. Then increments to get a new unique id
    new_id = str(max([int(profile[0]) for profile in profiles[1:]], default=-1) + 1)
    tables = { 'profile': [ [ ('profile_id', new_id) ] ] }
    for attribute, value in attributes:
        # profiles[0] = table head/attributes
        if attribute not in profiles[0]:
            if attribute not in tables:
                tables[attribute] = []
            tables[attribute].append([])
            tables[attribute][-1].append(('profile_id', new_id))
            tables[attribute][-1].append(('order', len(tables[attribute]) - 1))
            tables[attribute][-1].append((attribute, value))
        else:
            tables['profile'][0].append((attribute, value))
    for table, lines in tables.items():
        add_lines_to_table(username, table, dict(lines[0]).keys(), lines)

if __name__ == '__main__':
    if len(sys.argv) > 2:
        username = sys.argv[1]
        attributes_raw = sys.argv[2:]
        if os.path.exists(os.path.join(db_dir, username)):
            create_new_profile(username, attributes_raw)
        else:
            print('That user does not exist')
    else:
        print('Error: Scripts must be run with 2 or more parameters')
        sys.exit(1)
