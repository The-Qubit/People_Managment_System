#!/usr/bin/env python3

import sys
import os
import csv
from consts import db_dir

def create_attribute_csv(username):
    pass

def create_new_profile(username, attributes_raw):
    attributes = { attribute.split(':', 1)[0] : attribute.split(':', 1)[1] for attribute in attributes_raw }

    for attribute, value in attributes.items():


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
